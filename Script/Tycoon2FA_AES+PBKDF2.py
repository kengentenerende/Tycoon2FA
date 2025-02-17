import base64
from Crypto.Protocol.KDF import PBKDF2
from Crypto. Cipher import AES
from Crypto. Hash import SHA512

def decrypt_aes():
    a = "e56DOEMl3NQWNT+Hhu1fLF7FTrVkCM56sQnb8v0wNE8VlM8Cxw/oNCChujun5T61PlNjWm4n0vHtlWRxCr2e91y+uye5eqFEwE/wFB0ixC5zM8erqWWjRkwDGTBraiikcKciEYrM/42MgcqS+pMhsR5nz2CvmNZg8UlH39cfOwpTnhKsGxWN/GzQjafE8m0tVZAh5qlAhvopG2+5JRFmgWRSqBaCWZJY76jHvt5GlHVHhK8HfVJDezG1jqA8H3mdYrXYD+j9Uz6MqtfE0UwV2ykVhQ7IDVlr+kuqMtoe82L1q1T0v7GOOdTllrUyc38cIEs1yO+kzMfZnGf3jK81NEI/RDXdMxcyCnvz1UWcG3t5XjLMqcTzpRhH58VlR++x9w4Ht7Ke2+09awj6nf0flffhlnPDQdo+DOAbhWR974TFSj4CBrPgdpve2BK1IIbZZgSoQ+97PJYtywcZcIjb9UqgJ3cmipAgihM3Sb+lhWatnPreKkxWLMsphVwO/4p7fIuahuq28BdKjhml97cv3wklBpgQhvcYKHvavxL1EtG4Vk/GpqfLMnTdm82MAoLoZT8rhU5iInQYe8nwP+XFVvq4LhOMkj7EIdWlYM9YCdBLa7JvWDtZBhFKw5yb0Kn2cpw4P1wA4ix8snnydMXZDI8ds2ml2eYQeCDcpAHypOt8AjcGotT9CT4DVz+BW4fuKYM0FVL51odw9bY7E9FLA2M15EJ+I40SwhpTv21mSeoJIF/IVHqVpUmzbknEDPhBTCNx2kiQI28Uegcs2B4b6A9qaL5HhFtbyHhdZt5bFtKvEeIhm1MolaI1sPUL6i6Fk980raJkfkaS/6PPyLDCgQ=="
    b = "b6d7d154b2b66718a837c5797246df1d"
    c = "1776e27ffe8545aa8237e055a9a12b8e"
    d = "3736323433383133353832613935323631323763656330343337376230336462"

    iterations = 2000
    key_size = 32

    d_bytes = bytes.fromhex(d)
    b_bytes = bytes.fromhex(b)
    key = PBKDF2(d_bytes, b_bytes, dkLen=key_size, count=iterations, hmac_hash_module=SHA512)
    iv = bytes.fromhex(c)

    encrypted_data = base64.b64decode(a)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)

    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    print("", decrypted_data.decode('utf-8'))

if __name__ == "__main__":
    decrypt_aes()
