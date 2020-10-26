from dataclasses import dataclass

from hashlib import sha256
import time

@dataclass
class Transaction:
    sender: str  # ECDSA address of the sender
    recipient: str  # ECDSA address of the recipient
    amount: float  # Amount of Helix being transfered
    timestamp: float  # Time when transaction was made

    @staticmethod
    def new(cls, sender, recipient, amount):  # Static Method to create new Transactuib
        """
        If we make a method static using the @staticmethod decorator, we can call the method without initializing the class
        Now, we can create a new Transaction by doing Transaction.new(index, previous_hash, transactions)
        """
        return cls(
            sender=sender,
            recipient=recipient,
            amount=amount,
            timestamp=time.time()
        )

    def hash(self):  # Generate a unique sha256 hash of the transaction
        return sha256(
            f'{self.sender}{self.recipient}{self.amount}{self.timestamp}'.encode()
        ).hexdigest()
