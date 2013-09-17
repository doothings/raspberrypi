#Using it as a torrent box

###Pre-requisites

 1. Have Raspbian installed
 
 
###Steps

  1. ```sudo apt-get update```
      
     ```sudo apt-get upgrade```
     
  2. ```sudo apt-get install deluged```

     ```sudo apt-get install deluge-console```
     
  3.  Start the deluge daemon by running ```deluged```
      
      It creates the necessary files that we can now edit.
 
      Stop this after some time (5-10 seconds) by running ```sudo pkill deluged```
     
  4.  Now edit the auth file. But first create a backup.
     
     ```cp ~/.config/deluge/auth ~/.config/deluge/auth.copy````

      Editing the auth file. ```nano ~/.config/deluge/auth```
     
      Add a line at the bottom of the configuration file with the following convention: ```user:password:level```
      
      Example : ```pi:pi:10``` (10 is full-access/administrative level for the daemon)
      
      
  5.  Now let's update the settings for allowing remote connections.
  
        deluged

        deluge-console
      
        config -s allow_remote True

        config allow_remote

        exit
      
  6.  Restart deluged for this configuration to take effect.
    
        sudo pkill deluged

        deluged
      
  7.  Intall deluge-web to be able to access it from remote.
  
        sudo apt-get install python-mako
  
        sudo apt-get install deluge-web
  
        deluge-web
        
  8.  Access deluge-web from a remote machine on the same network.
  
      Navigate to ```http://<rasberrypi-ip>:8112/``` . 

      You have a torrent server at your service!
      
      Enter the password from step 3 and immediately change it.
