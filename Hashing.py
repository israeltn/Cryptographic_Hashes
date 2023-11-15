import hashlib

class HashedAuthenticationSystem:
    def __init__(self):
        self.secret_key = input("Enter secret key: ")

    def generate_hash(self, message):
        # Concatenate the message and the secret key
        data_to_hash = message + self.secret_key

        # Use SHA-256 as the hash function (you can choose a different one if needed)
        hashed_data = hashlib.sha256(data_to_hash.encode()).hexdigest()

        # Append the hash to the original message
        authenticated_message = message + hashed_data

        return authenticated_message

    def verify_hash(self, authenticated_message):
        # Extract the original message and the appended hash
        message = authenticated_message[:-64]  # Assuming a 64-character SHA-256 hash

        # Recompute the hash using the stored secret key
        computed_hash = self.generate_hash(message)[-64:]

        # Compare the computed hash with the extracted hash
        return computed_hash == authenticated_message[-64:]

# Example usage:
# A and B share a secret key
hashed_auth_system = HashedAuthenticationSystem()

# A generates an authenticated message
original_message = input("Enter message: ")
authenticated_message = hashed_auth_system.generate_hash(original_message)

# A sends the authenticated message to B

# B verifies the authenticity of the message
is_authentic = hashed_auth_system.verify_hash(authenticated_message)

if is_authentic:
    print("The message is authentic. Original Message:", original_message, "Hashed Key:", authenticated_message[-64:])
else:
    print("The message is not authentic. Possible tampering detected.")

