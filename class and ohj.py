#class and object ref access
class c203:
    course='PFS'
    TIMING='4.30'
    BATCH="M17"
sindhiya=c203()
#object access
print(sindhiya.course)
#CLASS ACCESS
print(c203.BATCH)
#MODIFYIING THE CLASS AND OBJECT
sindhiya.TIMING="4.00"
print(sindhiya.TIMING)
print(c203.TIMING)
c203().TIMING="5.00"
print(c203.TIMING)
print(sindhiya.TIMING)
