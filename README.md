# btc-wallet-generator

A simple Bitcoin wallet generator that generates a Bitcoin wallet address and private key. It is written in Python and uses the `bitcoin` library to generate the keys. It also uses a FastAPI server to serve the keys via an API endpoint.

## Getting Started

To get started, clone the repository and install the dependencies.

```bash
git clone https://github.com/engageintellect/btc-wallet-generator
cd btc-wallet-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

**NOTE:** You can also run the Next.js frontend client code. You can find the code [here](https://github.com/engageintellect/wally)
