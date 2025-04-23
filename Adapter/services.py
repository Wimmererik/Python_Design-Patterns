### Services to translate between

# Legacy transfer system
class LegacyTransferSystem:
    """Transfers expect source, target and amount to be given as separate parameters."""

    def transfer(self, 
                 source_account, 
                 target_account, 
                 amount):
        print(f"Transferring {amount}€...")
        if source_account.withdraw(amount):
            target_account.deposit(amount)
            print(f"Transfer complete")
            return True
        else:
            print(f"Transfer failed: Insufficient funds")
            return False


# Modern transfer system
class ModernTransferSystem:
    """
    Difference to legacy system:\n
    - Transfers expect a list containing source, target and amount to be given as a parameter.
    - Status messages are given as key:value pairs
    """

    def transfer(self, transfer_data):
        print(f"Processing transfer...")
        source = transfer_data[0]
        target = transfer_data[1]
        amount = transfer_data[2]
        
        if source.withdraw(amount):
            target.deposit(amount)
            return {"status": "success"}
        else:
            return {"status": "failed", "reason": "insufficient_funds"}
