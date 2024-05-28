import rsa

# Generate public and private keys
(public_key, private_key) = rsa.newkeys(512)

# Function to encrypt a message
def encrypt_message(message, pub_key):
    return rsa.encrypt(message.encode('utf8'), pub_key)

# Function to decrypt a message
def decrypt_message(encrypted_message, priv_key):
    try:
        return rsa.decrypt(encrypted_message, priv_key).decode('utf8')
    except rsa.DecryptionError:
        return "Decryption failed."

# Function to sign a message
def sign_message(message, priv_key):
    return rsa.sign(message.encode('utf8'), priv_key, 'SHA-1')

# Function to verify a signature
def verify_signature(message, signature, pub_key):
    try:
        rsa.verify(message.encode('utf8'), signature, pub_key)
        return True
    except rsa.VerificationError:
        return False

# Example Usage
message = "Akimova Dianara is the best teacher! :)"
encrypted_message = encrypt_message(message, public_key)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, private_key)
print(f"Decrypted: {decrypted_message}")

signature = sign_message(message, private_key)
print(f"Signature: {signature}")

# Verify the signature
is_valid = verify_signature(message, signature, public_key)
print(f"Signature valid: {is_valid}")

# Attempt to verify with a wrong message
wrong_message = "This is a different message."
is_valid_wrong = verify_signature(wrong_message, signature, public_key)
print(f"Signature valid for wrong message: {is_valid_wrong}")
