
# Question 9

"""
Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

"""
import zlib
s = bytes('hello world!hello world!hello world!hello world!','UTF-8')
t = zlib.compress(s,1)
print(t)
print(zlib.decompress(t))

