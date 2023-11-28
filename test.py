"""
for i in range(ord('A'), ord('Z')+1):
    print(chr(i))
"""
little = 'test'
for i in little:
    print(ord(i))

print('==================')
big = little.upper()
for i in big:
    print(ord(i))