import struct

f = open('D:\\PythonProject\\TesStringsFileEditor\\hearthfires_english.strings', 'rb')
count = f.read(4)
dataSize = f.read(4)
print("数据长度：%d" % struct.unpack("I", count))
print("数据块大小：%d" % struct.unpack("I", dataSize))


