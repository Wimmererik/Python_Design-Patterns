### Client that only interfaces with default system


class Client:
    def transfer(self,
                 transfer_system,       # System used for transfer
                 source_account,        # Account withdrawing amount
                 target_account,        # Account depositing amount
                 amount):               # Amount being transferred
        
        print(f"Performing transfer for {amount}€ from '{source_account.name}' to '{target_account.name}'...")

        print(f"\nBefore transfer:")
        print(f"- {source_account}")
        print(f"- {target_account}")
        
        success = transfer_system.transfer(source_account, target_account, amount)
        
        print(f"\nAfter transfer:")
        print(f"- {source_account}")
        print(f"- {target_account}")
        if success:
            print(f"Client Status: Success\n")
        else:
            print(f"Client Status: Failed\n")
