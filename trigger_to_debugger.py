#Debug a long-running process (see also recipe)
#Add the code below to the target process
#Call the listen function in the start
#From a shell send the signal
## os.kill(<pid>, signal.SIGUSR1)
## kill  -s SIGUSR1 9196

#the code below is from 
#https://stackoverflow.com/questions/132058/showing-the-stack-trace-from-a-running-python-application
#I didn't get quite an interactive debugging session, which might be due to configuration of /tmp

import code, traceback, signal

print(os.getpid())


def debug(sig, frame):
   """Interrupt running process, and provide a python prompt for
   interactive debugging."""
   d={'_frame':frame}         # Allow access to frame object.
   d.update(frame.f_globals)  # Unless shadowed by global
   d.update(frame.f_locals)

   i = code.InteractiveConsole(d)
   message  = "Signal received : entering python shell.\nTraceback:\n"
   message += ''.join(traceback.format_stack(frame))
   i.interact(message)

def listen():
   signal.signal(signal.SIGUSR1, debug)  # Register handler

listen()

#some work
while True: time.sleep(10)
