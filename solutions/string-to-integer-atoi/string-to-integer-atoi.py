class Solution:
    def myAtoi(self, s: str) -> int:
        output=[]
        i=0
        # Ignore starting Whitespace
        while i<len(s) and s[i]==" ":
            i+=1
        # checks sign
        if i<len(s) and (s[i]=="-" or s[i]=="+"):
            output.append(s[i])
            i+=1
        # Add digits
        while i<len(s) and s[i].isdigit():
            output.append(s[i])
            i+=1
        # Conversion 
        o="".join(output)
        # 32 bit check
        if len(output)==0 or (len(output)==1 and output[0] in "+-"):
            return 0
        else:
            final_output=int(o)

        if final_output<-2**31:
            return -2**31
        elif final_output>2**31-1:
            return 2**31-1
        else:
            return  final_output


          



        
        



            