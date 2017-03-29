## Print a list of functions

ea = ScreenEA()

for f in Functions(SegStart(ea),SegEnd(ea)):
    
	name = GetFunctionName(f)
	if name == "strcpy" or name == "sprintf" or name == "strncpy" or name == "wcsncpy" or name == "swprintf":
        for ref in CodeRefsTo(f, 0):
            fname = GetFunctionName(ref)
            print "%s:%x:%s" (fname, ref, name)			
		#end = GetFunctionAttr(f, FUNCATTR_END)
        #locals = GetFunctionAttr(f, FUNCATTR_FRSIZE)
        #print("Function: %s, starts at %x, ends at %x\n" %(name, f, end))
        #print("    Local variable area is %d bytes\n" %(locals))
