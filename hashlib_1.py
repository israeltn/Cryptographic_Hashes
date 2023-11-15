import hashlib

class HashedMessageAuth:
    def __init__(self):
        self.secret_key = input("Enter secret key: ")

    def generate_hash(self, message):
        # append the message and the secret key
        data_to_hash = message + self.secret_key

        # Using  SHA-256 hash function 
        hashed_data = hashlib.sha256(data_to_hash.encode()).hexdigest()

        # Add the hash to the original message
        authenticated_message = message + hashed_data

        return authenticated_message

    def verify_hash(self, authenticated_message):
        # get the original message and the appended hash
        message = authenticated_message[:-64]  # using a 64-character SHA-256 hash

        #hash using the stored secret key
        computed_hash = self.generate_hash(message)[-64:]

        # Compare the computed hash with the extracted hash
        return computed_hash == authenticated_message[-64:]


# share  secret key
hashed_auth = HashedMessageAuth()

# generate an authenticated message
original_message = input("Enter message: ")
auth_message = hashed_auth.generate_hash(original_message)

# authenticated message

# verify the authenticity of the message
is_authentic = hashed_auth.verify_hash(auth_message)

if is_authentic:
    print("Message is authentic. with Original Message:", original_message, "and Hashed Key:", auth_message[-64:])
else:
    print("Message is not authentic.")

