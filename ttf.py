'''
Get ttf file all unicode index
1.install FontForge 
2.run FontForge and select ttf file
3.File->Execute Script
4.Use this script to get all unicode index
'''


import fontforge

fp = open("D:/test.txt","w+")

fnt = fontforge.open("D:/template1.ttf")
for g in fnt.glyphs():
    fp.write(str(g.unicode)+",")

fp.close()