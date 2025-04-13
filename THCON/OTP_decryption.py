jpd_header  = "FFD8FFE000104A464946"
jpd_header = bytes.fromhex(jpd_header)

output_file = "picture.jpg.encrypted"

with open(output_file, "rb") as ofile:
    output_data = ofile.read()
otp_know = bytes([(output_data[k] ^ jpd_header[k]) for k in range(len(jpd_header))])

print(otp_know)
passwd = otp_know
input_file = "picture.jpg"
with open(input_file, "wb") as ifile:
    buffer = bytes([(output_data[k] ^ passwd[k % len(passwd)]) for k in range(len(output_data))])
    print(buffer)
    ifile.write(buffer)