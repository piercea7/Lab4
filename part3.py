## Print a list of functions
def funcalls(a,name):
    for ref in CodeRefsFrom(a, 1):
        reffunname = GetFunctionName(ref)
        if reffunname == "strcpy" or reffunname == "sprintf" or reffunname == "strncpy" or reffunname == "wcsncpy" or reffunname == "swprintf":
            print "%s:%s" % (name, reffunname)
            return			
        else:
            funcalls(ref,name)

    return 


for i in range(GetEntryPointQty()):
    ord = GetEntryOrdinal(i)
    #print "loop\n"
    if ord == 0:
        continue
    addr = GetEntryPoint(ord)
    name = GetFunctionName(addr)
    funcalls(addr,name)
#for f in Functions(SegStart(ea),SegEnd(ea)):
    
#	name = GetFunctionName(f)
	
 #       for ref in CodeRefsTo(f, 0):
  #          fname = GetFunctionName(ref)
   #         print "%s:%x:%s" (fname, ref, name)			
		#end = GetFunctionAttr(f, FUNCATTR_END)
        #locals = GetFunctionAttr(f, FUNCATTR_FRSIZE)
        #print("Function: %s, starts at %x, ends at %x\n" %(name, f, end))
        #print("    Local variable area is %d bytes\n" %(locals))
