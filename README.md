
This project models transmission dynamics into a social network with dyadic relationships based on the user inputed social interaction. Based on the one on one relationship , we assign the relationship a one on one tranfer chance , which is the probability of the transfer of the disease from either to the other if one happens to be infected by it.

The one on one tranfer chance is calculated by assigning the relationship a transfer factor , which is the ratio of the one on one transfer chance of this relationship to the average one on one transfer chance of a particular disease , also referred to as the reproduction number (R0) in epidemology.

Since due to human socialogy is relative , even dyadic relationships might have different intensities with respect to the people in it but we assign it a single factor.

# Objective: 
Model inputted data to a mapping with edge weights as one on one transfer chance


# Algorithm:
If no value is filled for a person by someone, filled value is to be assumed 0.

Calculate average deviation of each person by finding the difference in filled values for all connections of a person and the person itself and divide it by the number of connections , and thus repeating for each person.

For each relation ship take the weighted average of the induvidually filled values in the ratio of their average deviations.

# Pseudocode:


    function model_data_to_weighted_dyadic_relationships (average_transfer_chance , data) :
    
        
        for person = all people who filled data 
        
            for connection = all connections of person mapped to filled value by person
            
                deviation = difference of filled value by connection and person for each other 
                add deviation to previously logged value in total_deviation for both people if combination of person and connection has not been encountered before
                
        
        
        for person = all people in total_deviation:
        
            divide mapped value of a person in total deviation by the number of connection of person 
            
            
        name total_deviation as average_deviation
        
        
        for person = all people in average deviation
        
            for connection = all connections of person
            
                if person contact combination not previously logged to risk_mapping
                
                    risk = [(mapped value of person in average_deviation)*(filled value of contact by person)]  +  [(mapped value of contact  in average_deviation)*                               (filled value of contact by person)]
        
        return risk_mapping
                    
                    
                           
                
                
                       
            
            
        
        
            
            
        
  
                
              
              
              
            


