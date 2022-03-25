import unittest
import csv



def trac (a,b,lst):
    sumOfDiff=0
    cost = 0
    cost_s=0
    min = lst[0]
    have_trac_cost= False
    max_l = max(lst)

    if(len(lst)<2):
        return 0
   
    for _ in range(len(lst)):

        diffr = max_l - lst[0]
        cost_s += (diffr*a)
        if(lst[0]>min):
            sumOfDiff += (lst[0]-min)
            lst.pop(0)
            if(not have_trac_cost):
                have_trac_cost=True
                cost+=b
        elif(lst[0]<min):
            diff = min-lst[0]
            if(diff>sumOfDiff):
                need = diff - sumOfDiff
                sumOfDiff += need
                cost += (need * a)
            sumOfDiff-=diff
            lst.pop(0)
        else:
            lst.pop(0)
            
    while sumOfDiff>0:
        if(sumOfDiff>=min):
            sumOfDiff-=min
        else:
            diff = min - sumOfDiff
            cost+=(diff*a)
            sumOfDiff=0

    if cost_s > cost:
        return cost
    else:
        return cost_s


def open_file(name):
    file = open('F:\Program\Python\Jadi\Basic\quera110016\%s.csv' %name)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    result =int( rows.pop(0)[0])
    first_line = rows.pop(0)

    a= int(first_line[1])
    b = int(first_line[2])
    
    sec_line = rows.pop(0)
    sec_line = [int(i) for i in sec_line]
    return result,a,b,sec_line


class Test(unittest.TestCase):  

    # def test_fun1(self):
    #     result,a,b,sec_line = open_file('1')
    #     self.assertEqual(trac(a,b,sec_line),result)

    # def test_fun2(self):
    #     result,a,b,sec_line = open_file('2')
    #     self.assertEqual(trac(a,b,sec_line),result)

    # def test_fun3(self):
    #     result,a,b,sec_line = open_file('3')
    #     self.assertEqual(trac(a,b,sec_line),result)

    # def test_fun4(self):
    #     result,a,b,sec_line = open_file('4')
    #     self.assertEqual(trac(a,b,sec_line),result)

    # def test_fun5(self):
    #     result,a,b,sec_line = open_file('5')
    #     self.assertEqual(trac(a,b,sec_line),result)

    def test_fun7(self):
        result,a,b,sec_line = open_file('7')
        self.assertEqual(trac(a,b,sec_line),result)
    
    def test_fun8(self):
        result,a,b,sec_line = open_file('8')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun9(self):
        result,a,b,sec_line = open_file('9')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun10(self):
        result,a,b,sec_line = open_file('10')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun11(self):
        result,a,b,sec_line = open_file('11')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun12(self):
        result,a,b,sec_line = open_file('12')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun13(self):
        result,a,b,sec_line = open_file('13')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun14(self):
        result,a,b,sec_line = open_file('14')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun15(self):
        result,a,b,sec_line = open_file('15')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun16(self):
        result,a,b,sec_line = open_file('16')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun16(self):
        result,a,b,sec_line = open_file('16')
        self.assertEqual(trac(a,b,sec_line),result)

    def test_fun18(self):
        result,a,b,sec_line = open_file('18')
        self.assertEqual(trac(a,b,sec_line),result)

if __name__ == '__main__':
    unittest.main()