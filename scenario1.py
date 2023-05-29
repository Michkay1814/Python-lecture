# Deployment Script with Environment Selectio:
#the idea is to for you to develop apython script that 
# allow uaers to 
# select the deployment envronment (e.g ,development,
# staging or production) and performs different actions 
# based on their choice.
#use conditionals to check the selected environment and 
# execute specific deployment task according.
# this exercise will allow you to practice conditionals,
# function calls that we studied in the last lecture and
# code organization to automate the deployment process based
# on user inputs.
# proposse a function to deploy to development envronment

def deploy_to_develoment():
    print("deploying to development envronment")
    
    # propose  a function to deploy a staging environment
    
    def deploy_to_staging():
        print("deploying to staging environment")
        
# propose a function to deploy to production environment

def deploy_to_production():
    print("deploy to production environment")
    
    def deploy(environment):
        if environment=="development":
            deploy_to_develoment()
                       
        elif environment =="Staging":
          deploy_to_Staging
            

        elif environment == "production":
         deploy_to_production()
        else:
         print("Its an invalid environment. Please choos either staging, production or development")

             
             
            
            
            
            
            