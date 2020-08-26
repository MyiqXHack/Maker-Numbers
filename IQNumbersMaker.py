from random import randint
import sys
from time import sleep
words = '\033[0;35mWelcom To Code Maker IQ Numbers The:Developer:Al_kabby.@Hack_Kabbay '
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
keys = input('\033[0;32mENTER KEY 077,079,075: ')
R = int(input("\033[0;31mEnter range of numbers: "))
if keys == '077':
     def numbs(H):
     	range_s = 10**(H-1)	
     	range_e = (10**H)-1
     	return  randint(range_s,range_e)
     for KeYs in range(0,R):
     	print('0770',numbs(7))
elif keys == '079':
     def numbers(n):
     	  range_st = 10**(n-1)
     	  range_en = (10**n)-1
     	  return  randint(range_st,range_en)
     for KEYs in range(0,R):
     	  	print('0790',numbers(7))
elif keys == '075':
	 def Numbs(i):
	 	  range_sta = 10**(i-1)
	 	  range_end = (10**i)-1
	 	  return randint(range_sta,range_end)
	 for keyss in range(0,R):
	 	print('0750',Numbs(7))