position = ('MIT', 'Stanford', 'Harvard', 'Caltech', 'University of Chicago', 'University of Pennsylvania',
            'Princeton University', 'Yale University', 'Cornell University', 'Columbia Unversity',
            'Johns Hopkins University', 'University of Michigan', 'UCB', 'NYU', 'UCLA', 'Duke University',
            'Carnegie Mellon University', 'UCSD', 'Brown University', 'University of Texas at Austin')

void = ''

print(void)
print(f'\033[1mThe first 5 universities are:\033[m {position[0:5]}')
print(f"\033[1mThe last 4 universities are:\033[m {position[-4:]}")
print(void)
print("\033[1m\033[4mIn alphabetical order:\033[m\033[m")
for uni in sorted(position):
    print(uni)
print(void)
for loc, uni in enumerate(position):
    if 'Harvard' in uni:
        if loc == 0:
            print(f'Harvard is in 1st position')
        elif loc == 1:
            print(f'Harvard is in 2nd position')
        elif loc == 2:
            print(f'Harvard is in 3rd position')
        else:
            print(f'Harvard is in {loc + 1}th position')
        break
else:
    print('University not found.')

