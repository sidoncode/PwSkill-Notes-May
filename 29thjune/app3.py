import logging
logging.basicConfig(
    filename="app_log.txt",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#log message of different levels
logging.debug('Debug Message')
logging.info('info Message')
logging.warning('Warning Message')
logging.error('error Message')
logging.critical("Critical Message")

'''
log - debug: detailed information for diagnosing problems
log info: general info about the program startime / end time
log warning: indication of something unexpected
log critical: highest priority: serious / fatal problem in program
'''