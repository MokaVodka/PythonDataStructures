import math


# -- Experiment iv --
# Implement lin_reg(x, y) which returns coefficient m, k
# such that y = m + k ∗ x fits the input x, y data.
def lin_reg(xLst, yLst):
    size = len(xLst)
    sumX = sum(xLst)
    sumY = sum(yLst)
    sumXX = sum(list(x * x for x in xLst))
    sumXY = sum(list(xLst[i] * yLst[i] for i in range(size)))

    # Find best fit f(x) = slope * x + offset
    offset = (sumXX * sumY - sumX * sumXY) / (size * sumXX - sumX * sumX)
    slope = (size * sumXY - sumX * sumY) / (size * sumXX - sumX * sumX)

    return offset, slope


# -- Experiment v --
# Estimate the time complexity using the log-log and linear regression
# Print coefficient k
def get_polinomial_ordo(sizeLst, timeLst):

    # Get logs for sizes and times
    logSize = [math.log(size) for size in sizeLst]
    logTime = [math.log(time) for time in timeLst]

    # Find best fit straight line for logSize / logTime field
    offset, slope = lin_reg(logSize, logTime)
    lineY = [offset + slope * x for x in logSize]
    coefficient = slope
    bestFitLine = lineY, logSize, logTime

    coefficient = round(coefficient, 3)
    print(f'Coefficient k: {coefficient} | O(n^{round(coefficient)})')

    return coefficient, bestFitLine
