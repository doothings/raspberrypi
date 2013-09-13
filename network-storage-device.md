#Network Storage Device

###Pre-requisites 

 1. Plug-in the external hard-drives / usb drives to the RasPi using a USB hub or direclty.
 
 2. You can either work directly using the GUI or via the ssh connection.


###Steps

  1.  Add support to Rasbian for NTFS-formatted disks 
  
      ```sudo apt-get install ntfs-3g``` 
  
  2.  Are there unmounted partitions from the attached external hard drives?
  
      ```sudo fdisk -l```

  3. We need directories to mount the drives to
  
      ```sudo mkdir /media/hdd1```

      ```sudo mkdir /media/hdd2```

  4. Mount drives to these directories
  
      ```sudo mount -t auto /dev/sda1 /media/USBHDD1```

      ```sudo mount -t auto /dev/sdb1 /media/USBHDD2```
      
  5. Now install Samba to access contents over the network.
  
      ```sudo apt-get install samba samba-common-bin```
      
  6. Edit Samba config ```/etc/samba/smb.conf``` and enable security.
  
  7. Restart Samba ```sudo /etc/init.d/samba restart```
  
  8. 
