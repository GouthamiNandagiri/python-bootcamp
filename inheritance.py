'''inheritance types:
1.single
2.multiple
3.multilevel
4.hierachical
5.hybrid'''
'''
class JNTUH:
    def schedule_academic(self):
        print('scheduling academics')
    def declare_holidays(self):
        print('National and summer Holidays')
    def results(self):
        print('go to www.jntuhresults.com')
class Sridevi(JNTUH):
    def fees(self):
        print('3rd year fee is 85k')
jobj=JNTUH()
jobj.results()
#jobj.fees()
s1=Sridevi()
s1.schedule_academic()
s1.declare_holidays()
'''


