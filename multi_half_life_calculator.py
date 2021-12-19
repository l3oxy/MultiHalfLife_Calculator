'''
Multi Half-lifes Calculator
See "https://github.com/l3oxy/MultiHalfLife_Calculator"
'''

import datetime
import math

halflife = datetime.timedelta(hours=12) # AKA T1/2 or T-half
dose = 100
dosing_frequency = datetime.timedelta(days=1) # AKA time between doses
sample = datetime.timedelta(weeks=10)
quantity_of_doses = round(sample / dosing_frequency)
print("quantity_of_doses: " + str(quantity_of_doses))

# Determine all of the dose dates
dosing_record = [] # dosing datetimes. In the future this will likely contain instead an object for each dosing, and each object will contain the dose and datetime.
for dose_number in range(quantity_of_doses):
    time_until_said_dose = dosing_frequency * dose_number # how far into the future will this dosing occur.
    said_dose_datetime = datetime.datetime.now() + time_until_said_dose
    dosing_record.append(said_dose_datetime)
print(dosing_record)

# For a given datetime, determine the serum concentration at said datetime,
# by looking at each dosing and determining how much substance from said dosing is
# remaining at said datetime (after the half-lifes), and then summing them all.
serum_concentration = 0
sample_date = datetime.datetime.now() + sample
for i in range(len(dosing_record)):
    print("[" + str(i) + "] " + "dose: " + str(dosing_record[i]))
    duration_since_this_dosing = sample_date - dosing_record[i]
    quantity_of_halflifes_for_this_dosing = duration_since_this_dosing / halflife #FIXME RFE WARNING:  This does not account for partial half lifes, i think!!
    print("[" + str(i) + "] " + "quantity_of_halflifes_for_this_dosing: " + str(quantity_of_halflifes_for_this_dosing))

    is_halflifes_between_dosing_and_sampledate_a_whole_number = quantity_of_halflifes_for_this_dosing.is_integer()
    if is_halflifes_between_dosing_and_sampledate_a_whole_number:
        this_dosings_dose_remaining_at_sample_time = (dose * (0.5 ** quantity_of_halflifes_for_this_dosing)) # FIXME test this. idek if this is correct.
    else:
        # https://www.mathcentre.ac.uk/resources/uploaded/half-lives.pdf
        # find half-life number below/previous, & datetime, & the serum concentration remaining at that time (e.g. 225)
        previous_halflife_number = math.floor(quantity_of_halflifes_for_this_dosing)
        previous_halflife_serum_concentration = (dose * (0.5 ** previous_halflife_number))
        print("[" + str(i) + "] " + "previous_halflife_serum_concentration : " + str(previous_halflife_serum_concentration))
        # find half-life number above/next, & datetime, & the serum concentration remaining at that time (e.g. 450)
        next_halflife_number = math.ceil(quantity_of_halflifes_for_this_dosing)
        next_halflife_serum_concentration = (dose * (0.5 ** next_halflife_number))
        print("[" + str(i) + "] " + "next_halflife_serum_concentration : " + str(next_halflife_serum_concentration))
        # calculate the difference between these serum concentration levels (e.g. 450 - 225 = 225)
        serium_concentration_difference_between_previous_halflife_and_next_halflife = previous_halflife_serum_concentration - next_halflife_serum_concentration
        # calculate what percentage of the way sample is between previous half-life and next half-life
        percentage_to_next_halflife = quantity_of_halflifes_for_this_dosing % 1
        print("[" + str(i) + "] " + "percentage_to_next_halflife : " + str(percentage_to_next_halflife))
        # multiply the difference
        the_difference = percentage_to_next_halflife * serium_concentration_difference_between_previous_halflife_and_next_halflife
        print("[" + str(i) + "] " + "the_difference : " + str(the_difference))
        # subtract from upper value
        this_dosings_dose_remaining_at_sample_time = previous_halflife_serum_concentration - the_difference

    serum_concentration += this_dosings_dose_remaining_at_sample_time
    print("[" + str(i) + "] " + "this_dosings_dose_remaining_at_sample_time: " + str(this_dosings_dose_remaining_at_sample_time))
    print("[" + str(i) + "] " + "New serum concentration: " + str(serum_concentration))
    print(" ")

print(str(sample_date) + " serum concentration: " + str(int(serum_concentration)))
