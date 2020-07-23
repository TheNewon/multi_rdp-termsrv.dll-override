# multi_rdp-termsrv.dll-override
## Allow multiple remote desktop connection + local connection.

# Windows 10 Enterprise only!
- Copy dll file to downloaded folder, run py or exe.
- Then rename original file to dll.bak to have a backup file.
- Edited file renames to original name to can copy to system32. (Probably you will need to change ownership of a file to replace it (make it 2 times. 1st for replacing 2nd to back to original owner))
- For orginal file in system32: 
--- change owner to your user
--- after changing owner to your user u must add your user with full control.
--- then copy edited file.
--- then turn off inheritance
--- then delete your user from list
--- then change owner to orginal
--- NT SERVICE\TrustedInstaller  <-- orginal owner
--- then turn on inheritance and delete duplicat on list that aren't from inheritance.
- After windows update you will need to do it again.
### (Rdp local helps while you need to make a python bot using the mouse and keyboard and you wanna have it separate in one window) <---- example of use
