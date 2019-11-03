class NumSeq:
    numdict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
               9: "Nine", \
               10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", \
               17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", \
               60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    bigs = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion']

    @staticmethod
    def dbldig(num):
        tens, below_ten = divmod(num, 10)
        return ((NumSeq.numdict[tens * 10] + '-' + str(NumSeq.numdict[below_ten].lower())))

    @staticmethod
    def tpldig(num):
        hundreds, tens = divmod(num, 100)
        tenssep = NumSeq.dbldig(tens)

    @staticmethod
    def num2txt(num):
        """This method uses dictionary and array to function to print numbers to text"""
        if num < 0:
            raise ValueError("Must use positive integers")
        if (num == 0):
            return (NumSeq.numdict[num])
        if(1 <= num <= 19):
            return(NumSeq.numdict[num])
        elif (20 <= num <= 99):
            return NumSeq.dbldig(num)
        #WIP.
        # Thinking I need to turn the two digit and 3 digit into separate functions to call for each 3 digit integer return?
        # Below isn't working.
        # Call the two digit for less than 20 with following special cases:
        # Address: 0 in tens for [01, 02,03,04,05,06,07,08,09,]
        # Address: adding the word "and " for the above as well as [10,11,12,13,14,15,16,17,18,19]
        # Call the two digit for greater than 20
        elif(100 <= num <= 999):
            hundreds, tens = divmod(num, 100)
            tenssep=NumSeq.dbldig(tens)
            #if (00 <= num <= 09):
                #sngl = divmod(num, 10)
                #return NumSeq.numdict[hundreds] + ' hundred and ' + tenssep.lstrip('0')
            if num == 10:
                return NumSeq.numdict[hundreds] + ' hundred' + tenssep.rstrip('0')
            elif (11 <= num <= 19):
                return NumSeq.numdict[hundreds] + ' hundred' + str(NumSeq.numdict[num])
            elif (20<=num<=99):
                return NumSeq.numdict[hundreds] + ' hundred' + tenssep
            # if 20 <= num <=99:
            #     tens, below_ten = divmod(num, 10)
            # return(((numdict[hundreds] + 'hundred ' + (numdict[tens * 10] + '-' + str(numdict[below_ten].lower)))))

        #WIP - All the Bigs (pairs of 3)

        #while(num > 999)
            #num =