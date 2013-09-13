#Using it as a torrent box

###Pre-requisites

 1. Have Raspbian installed
 
 
###Steps

  1. ```sudo apt-get update```
      
     ```sudo apt-get upgrade```
     
  2. ```sudo apt-get install deluged```

     ```sudo apt-get install deluge-console```
     
  3. ```cp ~/.config/deluge/auth ~/.config/deluge/auth.copy````

     ```nano ~/.config/deluge/auth```
     
      Add a line at the bottom of the configuration file with the following convention:

      ```user:password:level```
      
      Example: ```pi:pi:10``` [10 is full-access/administrative level for the daemon]
      
  4. ```deluged```

      ```deluge-console```
      
      ```config -s allow_remote True```

      ```config allow_remote```

      ```exit```
      
  5.  ```sudo pkill deluged```

      ```deluged```
      
  6.  ```sudo apt-get install deluged

        sudo apt-get install python-mako

        sudo apt-get install deluge-web

        deluge-web```
        
  7.  Access deluge-web from a remote machine on the same network.
  
      Navigate to http://<raspi-ip>:8112/ . You have a torrent server at your service!
