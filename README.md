# FTP_Walker

I needed a function like os.walk on FTP and there where not any so i thought it would be useful to write it 

## how to use:

first connect to your host : 

    host_address = "my host address"
    user_name = "my username"
    password = "my password"


    ftp = FTP(host_address)
    ftp.login(user=user_name,passwd=password)
    
now you can call the function like this:

	ftpwalk = FTP_Walker("FTP root path","path to local") # I'm not using path to local yet but in future versions I will improve it. so you can just path an '/' to it 
	
and then to print and download files you can do somthing like this :

	for item in ftpwalk:
    ftp.retrbinary("RETR "+item, open(os.path.join(current_loc,item.split('/')[-1]),"wb").write) #it is downloading the file 
    print(item) # it will print the file address
note: I am working on it to give you more options , so if you have any idea that is usefull for users to have it in FTP_Walker i'll be happy to hear that , thank you
