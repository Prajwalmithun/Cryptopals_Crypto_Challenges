import sys
sys.path.insert(0, '../..')
sys.path.insert(0, '../')
sys.path.insert(0, './')
import Function
import base64

"""
>>> Implement CBC mode

    CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, 
    despite the fact that a block cipher natively only transforms individual blocks.

    In CBC mode, each ciphertext block is added to the next 
    plaintext block before the next call to the cipher core.

    The first plaintext block, which has no associated previous ciphertext block, 
    is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

    Implement CBC mode by hand by taking the ECB function you wrote earlier, 
    making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), 
    and using your XOR function from the previous exercise to combine them.

    The file here is intelligible (somewhat) when CBC decrypted 
    against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) 
"""

def task10():
    data = Function.File.LoadLines(__file__)
    
    # Stips newlines 
    for line in data:
        line = line.strip()

    data = "".join(data)

    iv = "00" * 16
    key = "YELLOW SUBMARINE"

    # Checks decryption and encryption
    plainText = Function.Encryption.AES.CBC_Decrypt(iv, key, data)
    cipherText = Function.Encryption.AES.CBC_Encrypt(iv, key, plainText)
    
    return cipherText

if __name__ == "__main__":
    task10()