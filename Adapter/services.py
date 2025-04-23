### Services to call or translate to


class DefaultTransferSystem:
    """Transfers expect source, target and amount parameters to be given separately."""

    def transfer(self, source_account, target_account, amount):
        print(f"Transferring {amount}€...")

        if source_account.withdraw(amount):
            target_account.deposit(amount)
            print(f"Transfer complete")
            return True
        else:
            print(f"Transfer failed: Insufficient funds")
            return False


class ListBasedTransferSystem:
    """
    Difference to default system:\n
    - Transfers expect a list containing source, target and amount to be given as a parameter
    - Status messages are given as dictionaries
    """

    def transfer(self, transfer_data):
        print(f"Processing transfer...")
        source = transfer_data[0]
        target = transfer_data[1]
        amount = transfer_data[2]
        
        if transfer_data[0].withdraw(transfer_data[2]):
            transfer_data[1].deposit(transfer_data[2])
            return {"status": "success"}
        else:
            return {"status": "failed", "reason": "insufficient_funds"}
