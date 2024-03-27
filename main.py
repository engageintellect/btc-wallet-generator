from fastapi import FastAPI
from mnemonic import Mnemonic
from bitcoin import *
from hdwallet import BIP32HDWallet
import uvicorn

app = FastAPI()

# Generate a BIP39 seed phrase


def generate_seed_phrase():
    mnemonic = Mnemonic("english")
    # Generate a 128 bits BIP39 seed for a 12 word mnemonic
    return mnemonic.generate(128)  # Use 128 bits for 12-word seed phrase

# Generate a Bitcoin address and private key from a seed phrase


def generate_bitcoin_keys(seed_phrase):
    wallet = BIP32HDWallet()  # Initialize the wallet
    wallet.from_mnemonic(mnemonic=seed_phrase, language="english")

    # Specify the derivation path for the first address
    wallet.from_path("m/44'/0'/0'/0/0")

    private_key = wallet.private_key()
    # Ensure you're using the compressed public key
    public_key = wallet.public_key(compressed=True)

    # Generate P2PKH address from the compressed public key
    # 0 is the magic byte for mainnet
    address = pubtoaddr(public_key, magicbyte=0)

    return private_key, address


@app.get("/api/walletGen")
def generate_wallet():
    # Generate a seed phrase
    seed_phrase = generate_seed_phrase()

    # Generate a Bitcoin private key and address from the seed phrase
    private_key, bitcoin_address = generate_bitcoin_keys(seed_phrase)

    # Convert the private key to WIF format (compressed)
    private_key_wif = encode_privkey(
        decode_privkey(private_key, 'hex'), 'wif_compressed')

    # Return the seed phrase, Bitcoin WIF private key, and Bitcoin address
    payload = {
        "btcAddress": bitcoin_address,
        "privateKey": private_key_wif,
        # "seedPhrase": seed_phrase
    }

    return payload


# Check if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the Uvicorn server with the FastAPI app, enabling auto-reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
