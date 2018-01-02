from base64 import urlsafe_b64encode
from binascii import hexlify
from keccakhash import KeccakHash
from keccak import Keccak

_SPONGE_ABSORBING = Keccak._SPONGE_ABSORBING

class Shake(KeccakHash):

    """A SHAKE variable-output-length function."""

    def digest(self, n):
        if self.direction == _SPONGE_ABSORBING:
            self.pad()
        return self.squeeze(n)

    def hexdigest(self, n):
        return hexlify(self.digest(n))

    def b64digest(self, n):
        return urlsafe_b64encode(self.digest(n))