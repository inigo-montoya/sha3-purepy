from keccak import Keccak

_SPONGE_ABSORBING = 1
_SPONGE_SQUEEZING = 2

class KeccakHash(object):

    def __init__(self, b='', rate=None, dsbyte=None):
        if rate < 0 or rate > 199:
            raise Exception("Invalid rate.")
        self.rate, self.dsbyte, self.i = rate, dsbyte, 0
        self.k = Keccak()
        self.buf = np.zeros(200, dtype=np.uint8)
        self.absorb(b)
        self.direction = _SPONGE_ABSORBING

    def absorb(self, b):
        todo = len(b)
        i = 0
        while todo > 0:
            cando = self.rate - self.i
            willabsorb = min(cando, todo)
            self.buf[self.i:self.i + willabsorb] ^= \
                np.frombuffer(b[i:i + willabsorb], dtype=np.uint8)
            self.i += willabsorb
            if self.i == self.rate:
                self.permute()
            todo -= willabsorb
            i += willabsorb

    def squeeze(self, n):
        tosqueeze = n
        b = b''
        while tosqueeze > 0:
            cansqueeze = self.rate - self.i
            willsqueeze = min(cansqueeze, tosqueeze)
            b += self.k.state.view(
                dtype=np.uint8)[
                self.i:self.i +
                willsqueeze].tostring()
            self.i += willsqueeze
            if self.i == self.rate:
                self.permute()
            tosqueeze -= willsqueeze
        return b

    def pad(self):
        self.buf[self.i] ^= self.dsbyte
        self.buf[self.rate - 1] ^= 0x80
        self.permute()

    def permute(self):
        self.k.state ^= self.buf.view(dtype=np.uint64)
        self.k.F1600()
        self.i = 0
        self.buf[:] = 0

    def update(self, b):
        if self.direction == _SPONGE_SQUEEZING:
            self.permute()
            self.direction == _SPONGE_ABSORBING
        self.absorb(b)
        return self

    def __repr__(self):
        return "KeccakHash(rate={}, dsbyte=0x{:02x})".format(
            self.rate, self.dsbyte)
