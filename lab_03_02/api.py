# from flask import Flask, request, jsonify
# from cipher.rsa.rsa_cipher import RSACipher  # Import chính xác class RSACipher
# from cipher.ecc import ECCCipher
# import sys
# import os


# ===================================== RSA =================================================
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# app = Flask(__name__)

# # Khởi tạo đối tượng RSA Cipher
# rsa_cipher = RSACipher()

# # Route để tạo khóa RSA (public và private)
# @app.route('/api/rsa/generate_keys', methods=['GET'])
# def rsa_generate_keys():
#     rsa_cipher.generate_keys()  # Tạo cặp khóa RSA
#     return jsonify({'message': 'RSA keys generated successfully'})

# # Route để mã hóa thông điệp bằng RSA
# @app.route("/api/rsa/encrypt", methods=["POST"])
# def rsa_encrypt():
#     try:
#         data = request.json
#         message = data.get('message')  # Lấy thông điệp từ request
#         key_type = data.get('key_type')  # Lấy loại khóa ('public' hoặc 'private')
        
#         # Kiểm tra đầu vào hợp lệ
#         if not message or key_type not in ["public", "private"]:
#             return jsonify({'error': 'Invalid input data'}), 400

#         private_key, public_key = rsa_cipher.load_keys()  # Tải khóa

#         key = public_key if key_type == 'public' else private_key
#         encrypted_message = rsa_cipher.encrypt(message, key)  # Mã hóa thông điệp
#         return jsonify({'encrypted_message': encrypted_message.hex()})  # Chuyển thành hex để dễ xử lý

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route để giải mã thông điệp bằng RSA
# @app.route("/api/rsa/decrypt", methods=["POST"])
# def rsa_decrypt():
#     try:
#         data = request.json
#         ciphertext_hex = data.get('ciphertext')  # Lấy dữ liệu đã mã hóa
#         key_type = data.get('key_type')  # Loại khóa ('public' hoặc 'private')

#         if not ciphertext_hex or key_type not in ["public", "private"]:
#             return jsonify({'error': 'Invalid input data'}), 400

#         private_key, public_key = rsa_cipher.load_keys()  # Tải khóa
#         key = public_key if key_type == 'public' else private_key

#         ciphertext = bytes.fromhex(ciphertext_hex)  # Chuyển chuỗi hex về bytes
#         decrypted_message = rsa_cipher.decrypt(ciphertext, key)  # Giải mã thông điệp
#         return jsonify({'decrypted_message': decrypted_message})  # Trả về kết quả

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route để ký thông điệp bằng RSA
# @app.route('/api/rsa/sign', methods=['POST'])
# def rsa_sign_message():
#     try:
#         data = request.json
#         message = data.get('message')  # Lấy thông điệp cần ký

#         if not message:
#             return jsonify({'error': 'Message is required'}), 400

#         private_key = rsa_cipher.load_keys()[1]  # Tải khóa riêng tư để ký
#         signature = rsa_cipher.sign(message, private_key)  # Ký thông điệp
#         return jsonify({'signature': signature.hex()})  # Trả về chữ ký dưới dạng hex

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route để xác thực chữ ký RSA
# @app.route('/api/rsa/verify', methods=['POST'])
# def rsa_verify_signature():
#     try:
#         data = request.json
#         message = data.get('message')
#         signature_hex = data.get('signature')

#         if not message or not signature_hex:
#             return jsonify({'error': 'Message and signature are required'}), 400

#         public_key = rsa_cipher.load_keys()[0]  # Tải khóa công khai để xác thực
#         signature = bytes.fromhex(signature_hex)  # Chuyển chữ ký từ hex về bytes
#         is_verified = rsa_cipher.verify(message, signature, public_key)  # Xác minh chữ ký
#         return jsonify({'is_verified': is_verified})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Chạy ứng dụng Flask trên cổng 5000
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


#  =================================================== ECC =================================================================
from flask import Flask, request, jsonify

# from .rsa.rsa_cipher import RSACipher

from cipher.ecc import ECCCipher  #     Thêm vào đầu file

app = Flask(__name__)

# Khởi tạo đối tượng RSACipher và ECCCipher
# rsa_cipher = RSACipher()
ec_cipher = ECCCipher()

# Endpoint để tạo khóa RSA
@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'RSA keys generated successfully'})

# Endpoint để mã hóa RSA
@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    plain_text = data['plain_text']
    encrypted_message = rsa_cipher.encrypt(plain_text)
    return jsonify({'encrypted_message': encrypted_message})

# Endpoint để giải mã RSA
@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    decrypted_message = rsa_cipher.decrypt(cipher_text)
    return jsonify({'decrypted_message': decrypted_message})

# Endpoint để tạo khóa ECC
@app.route('/api/ecc/generate_keys', methods=['GET'])
def ec_generate_keys():
    ec_cipher.generate_keys()
    return jsonify({'message': 'ECC keys generated successfully'})

# Endpoint để ký thông điệp bằng ECC
@app.route('/api/ecc/sign', methods=['POST'])
def ec_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ec_cipher.load_keys()
    signature = ec_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

# Endpoint để xác thực chữ ký ECC
@app.route('/api/ecc/verify', methods=['POST'])
def ec_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ec_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ec_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

# Hàm main để chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)