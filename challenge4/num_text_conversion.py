class NumSeq:
    nums = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
            9: "Nine", \
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", \
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", \
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    bigs = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion']

    @staticmethod
    def dbl_dig(num):
        dbl_return = ""
        if num == 0:
            return ""
        tens, below_ten = divmod(num, 10)
        if 1 < tens:
            dbl_return += NumSeq.nums[tens * 10]
            if 0 < below_ten:
                dbl_return += '-' + NumSeq.nums[below_ten].lower()
        elif tens == 1:
            dbl_return += NumSeq.nums[10 + below_ten]
        elif tens == 0:
            dbl_return += NumSeq.nums[below_ten]
        return dbl_return

    @staticmethod
    def tpl_dig(num, use_and=True):
        tpl_return = ""
        if num == 0:
            return ""
        hundreds, tens = divmod(num, 100)
        tenssep = NumSeq.dbl_dig(tens)
        if 0 < hundreds:
            tpl_return += NumSeq.nums[hundreds] + ' hundred'
            if (0 < tens):
                if use_and:
                    tpl_return += ' and '
                tpl_return += tenssep.lower()
        elif hundreds==0:
            if use_and:
                tpl_return += ' and '
            tpl_return += tenssep.lower()
        return tpl_return.rstrip().lstrip()
    @staticmethod
    def get_tpl(num):
        """This method gets triplets and returns them in an array"""
        tpl = str(num)
        tpl = tpl[::-1]
        a = 0
        b = 0
        output_rtn = ['']

        for c in tpl:
            a += 1
            output_rtn[b] = c + output_rtn[b]
            if a == 3:
                output_rtn[b] = int(output_rtn[b])
                b += 1
                a = 0
                output_rtn.append('')
        if len(output_rtn[b]) < 3 and output_rtn[b]:
            output_rtn[b] = int(output_rtn[b])
        elif len(output_rtn[b]) == 0:
            del(output_rtn[b])
            b -= 1
        return output_rtn

    @staticmethod
    def num2txt(num):
        """This method uses both a dictionary and array and the use of functions to convert numbers to text"""
        if num < 0:
            raise ValueError("Must use positive integers")
        if num == 0:
            return (NumSeq.nums[num])
        if 1 <= num <= 19:
            return(NumSeq.nums[num])
        elif 20 <= num <= 99:
            return NumSeq.dbl_dig(num)
        elif 100 <= num <= 999:
            return NumSeq.tpl_dig(num)
        else:
            bigs_str = ''
            tpls = NumSeq.get_tpl(num)
            i = 0
            for t in tpls:
                if i == 0:
                    bigs_str += NumSeq.tpl_dig(tpls[0])
                    i += 1
                    continue

                if t != 0:
                    bigs_str = NumSeq.tpl_dig(i, False) + ' ' + NumSeq.bigs[i - 1] + ' ' + bigs_str
                    i += 1
                else:
                    i += 1
            return bigs_str.capitalize().lstrip().rstrip()

