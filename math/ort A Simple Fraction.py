class Solution:
	def fractionToDecimal(self, numerator, denominator):
		# Code here
		inte = numerator//denominator
		den = numerator%denominator
		if den == 0:
		    return inte
		has = {}
		ans = str(inte)+'.'
		while den!=0 and den not in has:
		        has[den] = len(ans)
		        den = den*10
		        integer = den//denominator
		        den = den%denominator
		        ans+=str(integer)
		if den == 0:
		    return ans
		return (ans[:has[den]])+'('+(ans[has[den]:])+')'
