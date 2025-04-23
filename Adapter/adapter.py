### Adapter to enable use of list based system with default client

from interface import TransferSystem


class TransferAdapter(TransferSystem):
    def __init__(self, list_system):
        self.system = list_system
    
    def transfer(self, source_account, target_account, amount):
        # Convert to list
        transfer_data = [source_account, target_account, amount]
        
        # Call function in list based system and convert result
        result = self.system.transfer(transfer_data)
        return result["status"] == "success"    # Client will not know reason for failure
