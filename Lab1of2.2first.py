def population_density(mass, volume):
    density = mass/volume
    return density


test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}\n".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# using the formula for density D = m/v