# OTPas_ouf
### Challenge: 
It seems like Zypherion and Mammoth, two XSS gang members neither known for their cleverness nor prudence just exchanged a message for a "vewy top secret much important" occasion. Knowing the IQ level this may be of much interest or not, but we cannot afford to take any chances so we need you to help us decrypt this message.
### Analysis:
- Create OTP (10 bytes)
- Use the data from input file, XOR it with OTP, and write the result to output file with the .encrypted extension
### Solution:
- Recovering an OTP. Because the JPG format has a fixed header, we can use it to XOR with the data from output file in order to guess OTP. [Reference](https://en.wikipedia.org/wiki/List_of_file_signatures)
- OTP: FFD8FFE000104A464946
- Use the data feom ouput file to XOR with OTP, get input file.
- Flag: THC{TheCakeIsALie}
  
