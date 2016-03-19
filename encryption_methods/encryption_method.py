class EncryptionMethod(object):
    """
    Interface for Encryption methods.
    """

    name = "method name"

    @staticmethod
    def encrypt(message):
        raise NotImplementedError()

    @staticmethod
    def decrypt(message):
        raise NotImplementedError()
