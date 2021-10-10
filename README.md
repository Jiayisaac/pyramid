DESCRIPTION

Pyramid scheme smart contract

Currently deployed to the Rinkeby Testnet

DEPENDENCIES

- Visual Studio Code: https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Brownie: https://eth-brownie.readthedocs.io/en/stable/install.html

TO INTERACT WITH THIS SMART CONTRACT

- Install above dependencies

- Create a new folder pyramid and open this folder in Visual Studio Code

- Open a new terminal window and enter:  
    - brownie pm install Jiayisaac/pyramid@0.0.2

- Edit the .env file to select the network you would like to deploy to {rinkeby, kovan, goerli, ropsten, development, mainet-fork etc}
    - brownie run scripts/deploy.py

- To interact with the contract do so over etherscan, or via
    - brownie run scripts/subscribe.py
