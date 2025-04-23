### Adapter to enable use of modern system with legacy client

class TransferAdapter:
    def __init__(self, modern_system):
        self.system = modern_system
    
    def transfer(self, source_account, target_account, amount):
        # Convert to expected format
        transfer_data = [
            source_account,
            target_account,
            amount
        ]
        
        # Call the adapted system and convert the result
        result = self.system.transfer(transfer_data)
        return result["status"] == "success"
