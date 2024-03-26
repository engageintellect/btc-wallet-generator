from fastapi import FastAPI
from mnemonic import Mnemonic
from hdwallet import BIP32HDWallet
import uvicorn

app = FastAPI()

# Generate a BIP39 seed phrase


def generate_seed_phrase():
    mnemonic = Mnemonic("english")
    return mnemonic.generate(256)  # 256 bits is a standard BIP39 seed length

# Generate a Bitcoin address and private key from a seed phrase


def generate_bitcoin_keys(seed_phrase):
    wallet = BIP32HDWallet()  # Initialize the wallet
    wallet.from_mnemonic(mnemonic=seed_phrase)  # Set the mnemonic
    private_key = wallet.private_key()
    address = wallet.address()
    return private_key, address


@app.get("/api/walletGen")
def generate_wallet():
    # Generate a seed phrase
    seed_phrase = generate_seed_phrase()

    # Generate a Bitcoin private key and address from the seed phrase
    private_key, bitcoin_address = generate_bitcoin_keys(seed_phrase)

    # Return the seed phrase, Bitcoin private key, and Bitcoin address
    payload = {
        "btcAddress": bitcoin_address,
        "privateKey": private_key,
        "seedPhrase": seed_phrase
    }

    return payload


# Check if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the Uvicorn server with the FastAPI app, enabling auto-reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
