def FTP_Walker(FTPpath,localpath):
    os.chdir(localpath)
    current_loc = os.getcwd()
    for item in ftp.nlst(FTPpath):
        if not is_file(item):
            yield from FTP_Walker(item,current_loc)

        elif is_file(item):
            yield(item)
            current_loc = localpath
        else:
            print('this is a item that i could not process')
    os.chdir(localpath)
    return
    

def is_file(filename):
    current = ftp.pwd()
    try:
        ftp.cwd(filename)
    except Exception as e :
        ftp.cwd(current)
        return True
    
    ftp.cwd(current)
    return False
