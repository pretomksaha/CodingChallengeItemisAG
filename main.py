import salesTaxes
import conferenceTrack
import merchantGuide
def main():
    'Main Method to choose one of the problem and call that function to solve the problem.'
    'Input:'
    'wantTO: take a number input according to problem'
    'Output: print solution for choosing problems'
    while True:
        print('Select the problem you want to solve:')
        print('\tProblem 1: SALES TAXES \n\tProblem 2: CONFERENCE TRACK MANAGEMENT \n\tProblem 3: MERCHANT\'S GUIDE TO THE GALAXY \n\t4.exit')
        wantTo = input('Put a input number according to your choose:')

        try:
            if wantTo == '1':
                print(wantTo)
                salesTaxes.initialize()
            elif wantTo == '2':
                conferenceTrack.initialize()
            elif wantTo == '3':
                merchantGuide.initialize()
            else:
                break
        except:
            print('ERROR: Please Check your Input..')

if __name__ == "__main__":
    # execute only if run as a script
    main()
