class NumSeq:
    def __init__(self, number=0):
        self.number = number

    numdict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
               9: "Nine", \
               10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", \
               17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", \
               60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    bigs = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion']

    @staticmethod
    def dbldig(num):
        dbl_return = ""
        if num == 0:
            return ""
        tens, below_ten = divmod(num, 10)
        if 1 < tens:
            dbl_return += NumSeq.numdict[tens * 10]
            if 0 < below_ten:
                dbl_return += '-' + NumSeq.numdict[below_ten].lower()
        elif tens == 1:
            dbl_return += NumSeq.numdict[10 + below_ten]
        elif tens == 0:
            dbl_return += NumSeq.numdict[below_ten]
        return dbl_return

    @staticmethod
    def tpldig(num):
        tpl_return = ""
        if num == 0:
            return ""
        hundreds, tens = divmod(num, 100)
        tenssep = NumSeq.dbldig(tens)
        if 0 < hundreds:
            tpl_return += NumSeq.numdict[hundreds] + ' hundred'
            if (0 < tens):
                tpl_return += ' and ' + tenssep.lower()
        elif hundreds==0:
            tpl_return += ' and ' + tenssep.lower()
        return tpl_return

    @staticmethod
    def num2txt(num):
        """This method uses dictionary and array to function to print numbers to text"""
        if num < 0:
            raise ValueError("Must use positive integers")
        if num == 0:
            return (NumSeq.numdict[num])
        if 1 <= num <= 19:
            return(NumSeq.numdict[num])
        elif 20 <= num <= 99:
            return NumSeq.dbldig(num)
        elif 100 <= num <= 999:
            return NumSeq.tpldig(num)


        #WIP - All the Bigs (pairs of 3)

        #while(num > 999)
            #num =