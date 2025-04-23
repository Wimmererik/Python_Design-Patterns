### Client that only interfaces with legacy system

class Client:
    def transfer(self,
                 transfer_system,       # System used for transfer
                 from_account,          # Account withdrawing amount
                 to_account,            # Account depositing amount
                 amount):               # Amount being transferred
        
        print(f"Performing transfer for {amount}€ from '{from_account.name}' to '{to_account.name}'...")

        print(f"\nBefore transfer:")
        print(f"- {from_account}")
        print(f"- {to_account}")
        
        success = transfer_system.transfer(from_account, to_account, amount)
        
        print(f"\nAfter transfer:")
        print(f"- {from_account}")
        print(f"- {to_account}")
        if success:
            print(f"Status: Success\n")
        else:
            print(f"Status: Failed\n")
