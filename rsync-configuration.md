##Rsync setup.

 There are various approaches to have rsync running all the time.
 
 One is to run it as a daemon and the other is by configuring it via inetd/xinetd.
 
 But for both, we must first configure ```/etc/rsyncd.conf``` and create ```/etc/rsyncd.secrets``` for security.
 
 
###rsyncd.conf

  1. Create a file in /etc and call it rsyncd.conf.
  
  2. Open the file in your prefered editor
  
      sudo nano /etc/rsyncd.conf
      
    Add following fields to the file
    
      lock file = /var/run/rsync.lock
      log file = /var/log/rsyncd.log
      pid file = /var/run/rsyncd.pid

      [documents]
          path = /home/pi/torrentdata
          comment = The torrent folder on Pi
          uid = pi
          read only = no
          list = yes
          secrets file = /etc/rsyncd.secrets
          hosts allow = 192.168.0.0/255.255.255.0
