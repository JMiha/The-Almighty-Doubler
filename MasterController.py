#MasterController.py
#Presents the user with guidance allowing them to nominate a pathetic, small number as a candidate for doubling, and then passes the value to the PowerCore function (PowerCore.py) for processing.

from PowerCore import PowerCore
from ErrorAnalysis import ErrorAnalysis
from PseudoTransform import PseudoTransform
from PresentationRenderer import PresentationRenderer

def main():
    
    #Receive pathetic, small number from user
    print('Please present the puny number you wish to double:')
    pathetic_small_number = input()
    #TODO: Preclude letters/symbols/long or short or empty strongs/otherwise unsuitable strings
    
    #Inform user of number's acceptance
    print('Number successfully received. Initializing local doubling subroutines. Please wait.')
    
    #Call PseudoTransform operation to prepare number for PowerCore; overwrite value of pathetic, small number with improved value (though it is worth nothing that the number is still pathetic and small)
    pathetic_small_number = PseudoTransform(pathetic_small_number)
    
    #Call PowerCore to perform the doubling procedure; assign output
    almighty_doubled_number = PowerCore(pathetic_small_number)
    
    #Call PresentationRenderer to present the user with the almighty, doubled number
    PresentationRenderer(almighty_doubled_number)
    
    #Run error analysis
    ErrorAnalysis(pathetic_small_number, almighty_doubled_number)
    
    #Inform user that the doubling procedure is to be concluded
    print('Terminating doubling procedure.')
    
    #Return the user to their boring life
    return 



#Rudimetary Runtime Operation Scheduling System
if __name__ == "__main__":
    main()