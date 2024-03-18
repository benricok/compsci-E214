import math, stdio, binomial

def fail(s):
    stdio.writeln(s)

def assertAlmostEqual(a, b): # Assumes a and b are floats!
    if math.isnan(a) or math.isinf(a): fail("exceptional first double value as argument")
    if math.isnan(b) or math.isinf(b): fail("exceptional second double value as argument")
    if (((a * 0.9999) > b) or (b > (a * 1.0001))): fail(str(b) + " is not within 0.01% of " + str(a))

def testSmallValues():
    # The following probabilities are for the case where we flip one coin.
    # The probability that it will be heads is 50%, 50% tails.
    assertAlmostEqual(0.5, binomial.binomial(1, 0, 0.5))
    assertAlmostEqual(0.5, binomial.binomial(1, 1, 0.5))
    
    # The following probabilities are for the case where we flip two coins.
    # The probability that both will be heads is 25% (HH)
    # that one will be heads and the other tails is 50% (HT or TH)
    # that both will be tails is 25% (TT) 
    assertAlmostEqual(0.25, binomial.binomial(2, 0, 0.5))
    assertAlmostEqual(0.5, binomial.binomial(2, 1, 0.5))
    assertAlmostEqual(0.25, binomial.binomial(2, 2, 0.5))

    assertAlmostEqual(0.25412, binomial.binomial(8, 5, 0.7))

def testBigValues() :
    # If your code chokes on these, then you probably haven't been using logarithms
    # to prevent numerical overflow, you naughty person ;)
    assertAlmostEqual(1.3026e-05, binomial.binomial(100, 50, 0.3))
    assertAlmostEqual(0.057506, binomial.binomial(200, 80, 0.4))
    assertAlmostEqual(0.0025752, binomial.binomial(100000, 40000, 0.4))

def main():
    testSmallValues()
    testBigValues()

if __name__=='__main__': main()
