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
    - brownie pm install Jiayisaac/pyramid@0.0.3

- Edit the brownie-config.yaml file to select the default network you would like to deploy to {mainnet, rinkeby, kovan, goerli, ropsten, development, mainnet-fork etc}
    - brownie run scripts/deploy.py

- To interact with the contract do so over etherscan, or via
    - brownie run scripts/subscribe.py
