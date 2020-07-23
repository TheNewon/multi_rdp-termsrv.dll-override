import binascii
from_='39813C0600000F84'# partial value will be changed with others value next to it to get same index value
to_='B80001000089813806000090'
filename = 'termsrv.dll'
print('----------------opening-------------')
with open(filename, 'rb') as f:
    content = f.read()
    content_BA= bytearray(content)
print('------------------------------------')
print('-----------------copy---------------')
x=binascii.hexlify(content_BA)
print('-----------------info---------------')
bt=bytearray(bytes.fromhex(to_))
w=(content_BA).find(bytes.fromhex(from_))
print(w)
print(bytes(content_BA[w:w+len(bt)]))
print('-----------------dumy-changes-------')
for b in range(len(bt)):
    content_BA[w+b]=bt[b]
print('-----------------is-changed-?-------')   
y=binascii.hexlify(content_BA)
for i in range(len(x)):
    if x[i]!=y[i]:
        print('x: ',x[i],'y: ',y[i],'i: ', i)
if x==y:print('-----------------no-----------------')
if x!=y:
        print('-----------------yes----------------')
        with open('termsrv_edited.dll', 'wb') as fh:
            newFileByteArray = bytearray(content_BA)
            fh.write(newFileByteArray)
            
print('-----------------saved---------------')
input('press enter to exit')