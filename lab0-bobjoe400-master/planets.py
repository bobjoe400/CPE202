def weight_on_planets():
    # write your code here
    wht = float(input('What do you weigh on earth? '))
    mars = wht*0.38
    jupiter = wht*2.34

    print('\nOn Mars you would weigh {0:.2f} pounds.\nOn Jupiter you would weigh {1:.2f} pounds.'.format(mars,jupiter))
if __name__ == '__main__':
    weight_on_planets()
