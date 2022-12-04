// https://leetcode.com/problems/integer-to-english-words

from collections import deque

class Solution:
    def numberToWords(self, num: int) -> str:
        
        def thousandsToWords(num, place = 0):
            
            result = []
            if num == 0:
                return ''
            
            quotient, remainder = divmod(num, 100)
            if quotient:
                result.append(Ones[quotient] + " Hundred")
            
            if remainder < 20:
                if remainder:
                    result.append(Ones[remainder])
            else:
                quotient, remainder = divmod(remainder, 10)
                if quotient:
                    result.append(Tens[quotient])
                    if remainder:
                        result.append(Ones[remainder])

            result.append(Thousands[place])

            return ' '.join(result)
                
        Ones = 'Zero One Two Three Four Five Six Seven \
                Eight Nine Ten Eleven Twelve Thirteen Fourteen \
                Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        Tens = 'Blank Blank Twenty Thirty Forty Fifty Sixty \
                Seventy Eighty Ninety'.split()
        Thousands = ['','Thousand','Million','Billion']

        if num == 0:
            return "Zero"
        
        result = deque()
        quotient, remainder = divmod(num, 1000)
        interm_result = thousandsToWords(remainder)
        if interm_result:
            result.appendleft(interm_result)

        place = 1
        while quotient:
            quotient, remainder = divmod(quotient, 1000)
            interm_result = thousandsToWords(remainder, place)
            if interm_result:
                result.appendleft(interm_result)
            place += 1
        
        print(result)
        return ' '.join(result).strip()