# class TranspositionCipher:
#     def __init__(self):
#         pass
    
#     def encrypt(self, text, key):
#         encrypted_text = ""
#         for col in range(key):
#             pointer = col
#             while pointer < len(text):
#                 encrypted_text += text[pointer]
#                 pointer += key
#         return encrypted_text
    
#     def decrypt(self, text, key):
#         decrypted_text = [''] * key
#         row , col = 0,0
#         for symbol in text:
#             decrypted_text[col] += symbol
#             col += 1
#             if (col == key) or (col == key-1 and row >= len(text)%key): 
#                 col = 0
#                 row += 1
#         return ''.join(decrypted_text)
    
class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        # Calculate the number of rows needed
        rows = (len(text) + key - 1) // key
        
        # Initialize a list to hold the decrypted text rows
        decrypted_text = [''] * rows
        
        # Calculate the number of characters in each column
        chars_per_col = len(text) // key
        extra_chars = len(text) % key
        
        # Distribute the ciphertext characters into the rows
        index = 0
        for col in range(key):
            chars_in_this_col = chars_per_col + (1 if col < extra_chars else 0)
            for row in range(chars_in_this_col):
                decrypted_text[row] += text[index]
                index += 1
        
        # Join the rows to get the decrypted text
        return ''.join(decrypted_text)
