## first quesiton
i would append 4 zeros to the polynominal degree

the length of the polynomial is 5 (i.e., the binary string "10011" has 5 bits). The number of zeros to append is one less than this length, so 
5−1=4. But after padding the data with 4 zeros, the final CRC is calculated by dividing the augmented data by the generator polynomial.


## second quesiton

11010
10011 
------
01001   


## third quesiton

a) CRC can detect all single-bit errors:

True. CRC is designed to detect all single-bit errors. The polynomial is constructed in such a way that any single-bit error will produce a non-zero remainder when the data is divided by the polynomial.
b) CRC can detect all double-bit errors:

False. CRC can detect many double-bit errors, but it doesn't guarantee detection of all double-bit errors. Some double-bit errors may not change the remainder (depending on the positions of the errors and the polynomial used).
c) CRC can detect all burst errors shorter than the CRC length:

True. A burst error is a sequence of consecutive erroneous bits. If the burst error is shorter than the length of the CRC, it will be detected because the polynomial is designed to catch errors of this size.
d) CRC-32 is more reliable than CRC-16 for error detection:

True. CRC-32 is more reliable than CRC-16 because it uses a longer polynomial, which provides more error detection capabilities (it can catch a wider range of errors).


## 4


Original data: 1010
Transmitted data with CRC: 10100011 (this is the data sent with the CRC attached).
If we calculate the CRC over the original data 1010, and then compare it with the transmitted data 10100011, we can detect whether the error occurred during transmission.

The transmitted data includes the original data 1010 and the CRC 0011.
When performing the CRC calculation on the received data (10100011), we will see that the result will not match the expected CRC for 1010.
Therefore, the CRC check will detect the error because the remainder after performing the division will not be zero.
Conclusion: Yes, the CRC check will detect this error, because the error alters the remainder, which means the received data does not pass the CRC division check.






