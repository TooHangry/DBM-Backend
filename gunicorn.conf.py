bind = "127.0.0.1:9003"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/Users/robert.connolly/Desktop/DBM_Deploy/DBM-Backend/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/Users/robert.connolly/Desktop/DBM_Deploy/DBM-Backend/logs/gunicorn-access.log'
loglevel = 'debug'
workers = 4     # the number of recommended workers is '2 * number of CPUs + 1' 