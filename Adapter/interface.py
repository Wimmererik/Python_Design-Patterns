### Abstract base class as interface

from abc import ABC, abstractmethod


class TransferSystem(ABC):
    @abstractmethod
    def transfer(self, from_account, to_account, amount):
        pass
