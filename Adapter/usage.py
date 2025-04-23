### Example showcase of adapter

from account import Account
from adapter import TransferAdapter
from client import Client
from services import LegacyTransferSystem, ModernTransferSystem


if __name__ == "__main__":

    # Create accounts
    account_1 = "Acc_1", 2000
    account_2 = "Acc_2", 1500

    acc_1 = Account(account_1[0], account_1[1])
    acc_2 = Account(account_2[0], account_2[1])


    # Create legacy Client
    client = Client()


    print("\nUSING LEGACY TRANSFER SYSTEM:")
    legacy_system = LegacyTransferSystem()
    client.transfer(legacy_system, acc_1, acc_2, 300.52)

    # Reset accounts
    acc_1 = Account(account_1[0], account_1[1])
    acc_2 = Account(account_2[0], account_2[1])


    print("\nUSING MODERN TRANSFER SYSTEM THROUGH ADAPTER:")
    modern_system = ModernTransferSystem()
    adapter = TransferAdapter(modern_system)
    client.transfer(adapter, acc_1, acc_2, 300.52)

    # Reset accounts
    acc_1 = Account(account_1[0], account_1[1])
    acc_2 = Account(account_2[0], account_2[1])


    print("\nATTEMPTING TO USE MODERN TRANSFER SYSTEM WITHOUT ADAPTER:")
    modern_system = ModernTransferSystem()
    adapter = TransferAdapter(modern_system)
    #client.transfer(modern_system, acc_1, acc_2, 300.52) # This causes an error (on purpose)
