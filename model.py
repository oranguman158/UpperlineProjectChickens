def get_amount_chicken(w):
    return int(w)*5

def how_many_slaps(mass_chicken_g):
    heat_capacity = 2.72
    velocity = 4.0
    mass_hand = 467.2
    K = (1.0/2)*mass_hand*(velocity**2)
    factor = 1.0/2
    deltaT = (factor*K)/(mass_chicken_g*1000*heat_capacity)
    #Assuming getting a chicken to 400 degrees cooks it
    return 400.0/deltaT
    #start = 23
