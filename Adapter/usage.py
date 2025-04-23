### Example showcase of adapter

from account import Account
from adapter import TransferAdapter
from client import Client
from services import DefaultTransferSystem, ListBasedTransferSystem


if __name__ == "__main__":
    account_1 = "Acc_1", 2000
    account_2 = "Acc_2", 1500
    transfer_amount = 2300.52

    acc_1 = Account(account_1[0], account_1[1])
    acc_2 = Account(account_2[0], account_2[1])

    client = Client()

    print("\nUSING DEFAULT TRANSFER SYSTEM:")
    default_system = DefaultTransferSystem()
    client.transfer(default_system, acc_1, acc_2, transfer_amount)

    # Reset accounts
    acc_1 = Account(account_1[0], account_1[1])
    acc_2 = Account(account_2[0], account_2[1])

    print("\nUSING LIST BASED TRANSFER SYSTEM THROUGH ADAPTER:")
    list_system = ListBasedTransferSystem()
    adapter = TransferAdapter(list_system)
    client.transfer(adapter, acc_1, acc_2, transfer_amount)

    # Uncommenting the following results in an error, as ListBasedTransferSystem does not implement TransferSystem
    print("\nATTEMPTING TO USE LIST BASED TRANSFER SYSTEM DIRECTLY (will cause an error):")
    client.transfer(list_system, acc_1, acc_2, transfer_amount)
