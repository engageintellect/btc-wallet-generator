#!/usr/bin/env python3
import os
from mnemonic import Mnemonic
from hdwallet import BIP32HDWallet

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


if __name__ == "__main__":
    # Generate a seed phrase
    seed_phrase = generate_seed_phrase()

    # Generate a Bitcoin private key and address from the seed phrase
    private_key, bitcoin_address = generate_bitcoin_keys(seed_phrase)

    # Print the seed phrase, Bitcoin private key, and Bitcoin address
    print("Bitcoin Address:", bitcoin_address)
    print("Private Key:", private_key)
    print("Seed Phrase:", seed_phrase)
