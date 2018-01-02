from base64 import urlsafe_b64encode
from binascii import hexlify
from keccakhash import KeccakHash
from keccak import Keccak

_SPONGE_ABSORBING = Keccak._SPONGE_ABSORBING

class Sha3(KeccakHash):

    """An SHA-3 fixed-output-length function."""

    def digest(self):
        if self.direction == _SPONGE_ABSORBING:
            self.pad()
        return self.squeeze((200 - self.rate) // 2)

    def hexdigest(self):
        return hexlify(self.digest())

    def b64digest(self):
        return urlsafe_b64encode(self.digest())