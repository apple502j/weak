"""
 This library has two functions: One to generate a key, the other to actually
encrypt/decrypt something. The first function is generateKeys() which will
return a tuple of the public key and the private key. It will always return
different values. The second function is crypt(text,key). The public key is
needed when decrypting something encrypted via private key; same as private
key. When a wrong key is passed, it will return an exception.
"""

from .crypto import generateKeys, crypt

__all__ = ['generateKeys', 'crypt']
