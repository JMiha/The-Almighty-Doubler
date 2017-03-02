#ErrorAnalysis.py
#Performs quantitative error analysis on the results obtained from the main program and automatically provides the user with an accuracy report
def ErrorAnalysis(pathetic_small_number, almighty_doubled_number):
    #Inform the user that Error Analysis will now be performed
    print('Error Analysis Initializing -- Please Wait')

    #Generate a Comprehensive Error Evaluation Tensor (CEET) via Numerical Cross-Referencing (NCR)
    #NOTE: Through systematic workflow pipeline optimization, the CEET has been reduced down to a scalar value. However, it is unclear if these premature optimizations will interfere with future project improvements, and may require a later reversion to the full original tensor.
    comprehensive_error_evaluation_tensor = pathetic_small_number*2
    
    #Perform an Ordinary Least Squares Numerical Optimization by computing the error discrepancy using an L2 Norm with Euclidean Distance
    #TODO: Replace OLS Optimization with a more substantial error approximation algorithm, utilizing more complex techniques
    OLS_NO_L2_ED_Error = (1/2)*(almighty_doubled_number - comprehensive_error_evaluation_tensor)**2
    
    #Report the results of the Error Analysis to the user
    print('Error Analysis Complete!')
    print('The Almighty Doubler has successfully completed its task with an OLS_NO_L2_ED_Error of %2.7f.' % OLS_NO_L2_ED_Error)
    
    return 
    