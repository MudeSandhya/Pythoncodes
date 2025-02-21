#class and object ref access
class c203:
    course='PFS'
    TIMING='4.30'
    BATCH="M17"
sandhya=c203()
#object access
print(sandhya.course)
#CLASS ACCESS
print(c203.BATCH)
#MODIFYIING THE CLASS AND OBJECT
sandhya.TIMING="4.00"
print(sandhya.TIMING)
print(c203.TIMING)
c203().TIMING="5.00"
print(c203.TIMING)
print(sandhya.TIMING)
