@REM openssl req -new -x509 -newkey rsa:2048 -nodes -keyout server-key.key -out server-cert.crt -days 365 -config server-cert.cnf

# Tạo thư mục chứa chứng chỉ
mkdir certificates

# Tạo chứng chỉ tự ký cho server (valid 1 năm)
openssl req -x509 -newkey rsa:4096 -keyout certificates/server-key.key -out certificates/server-cert.crt -days 365 -nodes -subj "/CN=localhost"