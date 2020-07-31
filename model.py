def get_amount_chicken(w):
    return int(w)*3


def how_many_slaps(mass_chicken_Kg, speed):
    heat_capacity_Kg = 2720
    velocity = speed
    mass_hand = 0.467
    K = (1.0/2.0)*mass_hand*(velocity**2)
    factor = 1.0/2.0
    deltaT = (K)/(mass_chicken_Kg*heat_capacity_Kg)
    # Assuming getting a chicken to 400 degrees cooks it
    num=210.0/deltaT
    return int(num)
    # start = 23
