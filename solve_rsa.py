from Crypto.Util.number import *
import gmpy2

def next_prime2(n):
    num = n - 1
    while True:
        if isPrime(num):
            return num
        num -= 1
def next_prime1(n):
    num = n + 1
    while True:
        if isPrime(num):
            return num
        num += 1

factor = [115792089237316195423570985008687907853269984665640564039457584007913129619947,
115792089237316195423570985008687907853269984665640564039457584007913129622923,
115792089237316195423570985008687907853269984665640564039457584007913129592533,
115792089237316195423570985008687907853269984665640564039457584007913129565927,
115792089237316195423570985008687907853269984665640564039457584007913129541417,
115792089237316195423570985008687907853269984665640564039457584007913129526203,
115792089237316195423570985008687907853269984665640564039457584007913129507009,
115792089237316195423570985008687907853269984665640564039457584007913129472659]
n = 32317006071311007300714876688669951960444102669715484032130345427524654951631353355419877650806916212276402500548858834151025886661601982160629740366812343760839221218796456588791364620661035477524068742062486001097578134510998674555248555977747978320447065884046895815192913148345135256027099316122532348924259238397978283369582137813597737466275611732114098373554060037893185561621885934653748989988135247387463949515190516437670638317207973599216865318816980188306165655166925075452855367348439305737609452524641689752934451982713102744691251509730280711661703014774940296810705133733436287195960150698286350156051
'''
#use RsaCtfTools find p
d = p
while True:
    d = next_prime2(d)
    if n % d == 0:
        print d
        break
'''
phi = 1
e = 257
for i in factor:
    #print isPrime(i)
    phi = phi*(i-1)

d = gmpy2.invert(e,phi)
print (d*e)%phi
c = 0xe51dadb138bcfc8f132fb353cb49f1c8c5543f4e7b81a071882b1e278c7b96db88f2dc0a73b6cb4f827f3fe6b83344ab625c1060a36754eae25d1cf96a2885c6d81706ef9e041a9f7e4c688a65d35b47cdbb0aa8759c8e60f46a070c0dd289d57f4bf9b5f37a687c104d00bb4b732d26ab042b624431c071ab35e351613504fe4c2de6bc0d9be0a856f2f6d89a883c134351469f7489ad28cc6795e35dc6fb2e207c736d8d37863c09aec376e74af3ec37ae0d3b18083681989ad6394d6837fe66fccd506c85daf8b2b5ff3e544cc7098a1e3b67e5737037217fe7a0df79d002420db69c561d2f0c420d74898fd120540d32dfb63cf5059db2c7ef41697bcb8f
print long_to_bytes(pow(c,d,n))
