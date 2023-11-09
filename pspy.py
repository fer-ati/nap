#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice

class D:
	par = {

	 "A" : "E4YsW" ,
	 "B" : "sTy>," ,
	 "C" : "H+Ohc" ,
	 "D" : "?1^_3" ,
	 "E" : "li/1L" ,
	 "F" : "rM0X_" ,
	 "G" : "HiwS3" ,
	 "H" : "d!;^t" ,
	 "I" : "wS^LK" ,
	 "J" : "ZJ9mY" ,
	 "K" : "tYFdp" ,
	 "L" : "tp5Vm" ,
	 "M" : "kcW9I" ,
	 "N" : "oIPuk" ,
	 "O" : "G-!M," ,
	 "P" : "A/zpz" ,
	 "Q" : "!65G^" ,
	 "R" : "L?LE@" ,
	 "S" : "xr!jo" ,
	 "T" : "HNEPL" ,
	 "U" : "n;f$3" ,
	 "V" : "x>41C" ,
	 "W" : "FG9u7" ,
	 "X" : "cUe4x" ,
	 "Y" : "CXVdY" ,
	 "Z" : "L4@C<" ,
	 "a" : "OTlj_" ,
	 "b" : "zDUK," ,
	 "c" : "U3R5q" ,
	 "d" : "oP>0u" ,
	 "e" : "i%Bo?" ,
	 "f" : "Kw+W<" ,
	 "g" : "yCZiD" ,
	 "h" : "cT87Q" ,
	 "i" : "d#<Yz" ,
	 "j" : "E;o2I" ,
	 "k" : "Zf&hr" ,
	 "l" : "Kx3oy" ,
	 "m" : "JWA!>" ,
	 "n" : "y-u$4" ,
	 "o" : "b/--!" ,
	 "p" : "w#n%f" ,
	 "q" : "JSXQq" ,
	 "r" : "m>tX0" ,
	 "s" : "F!9$2" ,
	 "t" : "ZeA4j" ,
	 "u" : "uz3t:" ,
	 "v" : "L8_Gk" ,
	 "w" : "4JLY;" ,
	 "x" : "GH0xQ" ,
	 "y" : "ZpjvM" ,
	 "z" : "MmJ%w" ,
	 "1" : "5<MtO" ,
	 "2" : "NI'3u" ,
	 "3" : "iCEMq" ,
	 "4" : "a8<IG" ,
	 "5" : "T7-ez" ,
	 "6" : "yWa,r" ,
	 "7" : "yodFs" ,
	 "8" : "lZMn7" ,
	 "9" : "hi0IR" ,
	 "0" : "9530," ,
	 "!" : "ch:CF" ,
	 "@" : "pYVp/" ,
	 "#" : "M<f'T" ,
	 "$" : "RTJ>8" ,
	 "%" : "V?N80" ,
	 "^" : "E0AQX" ,
	 "&" : "6NJTc" ,
	 "*" : ",Q'*!" ,
	 "_" : "@Nvd*" ,
	 "-" : "RCf$f" ,
	 "+" : "jPGIk" ,
	 ":" : "jowu8" ,
	 ";" : "Canr2" ,
	 "'" : "LM^at" ,
	 ">" : "'5G1M" ,
	 "," : "oLY'%" ,
	 "<" : "/YARz" ,
	 "/" : "7KeYH" ,
	 "?" : "gdbBG" ,
	 "." : "cet4w" ,
	 " " : "wjR26"
	 
	}
	
	numeri = "1234567890"
	parole_h = "!@#$%^&*_-+:;'>,</?"
	parole_g = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	parole_p = "abcdefghijklmnopqrstuvwxyz"
	parole_gp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alf_g = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	alf_p = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	lista_completa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', ':', ';', "'", '>', ',', '<', '/', '?']


def nem():
	stringa = input("Inserisci una stringa: ")

	nuova_stringa = ""
	for lettera in stringa:
		
		if lettera in par:
			nuova_stringa += par[lettera]
		
		else:
			nuova_stringa += lettera

	print(f"La stringa sostituita è: {nuova_stringa}")

if __name__ == "__main__":
	nem()

''''''




















