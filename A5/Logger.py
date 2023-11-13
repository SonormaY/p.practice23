class Logger:    
    def printToFile(log_message = "", out_file = "out"):
        file = open(out_file, 'a')
        file.write(log_message)
        file.close()