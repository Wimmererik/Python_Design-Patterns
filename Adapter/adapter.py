### Adapter to enable use of modern system with legacy client

from interface import TransferSystem

class TransferAdapter(TransferSystem):
    def __init__(self, modern_system):
        self.system = modern_system
    
    def transfer(self, source_account, target_account, amount):
        # Convert to expected format
        transfer_data = [source_account, target_account, amount]
        
        # Call function in new system and convert result
        result = self.system.transfer(transfer_data)
        return result["status"] == "success"
