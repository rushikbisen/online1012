import logging
# logging.basicConfig(level=10,filename='server2.log',
#                     format='%(asctime)s - %(levelname)s -%(message)s',
#                     datefmt='%d-%m-%Y %H:%M:%S')
#logger = logging.getLogger("gold.py")

# logging.critical("critical message")
# logging.error("error message")
# logging.warning("warning message")
# logging.info("info message")
# logging.debug("debug message")


from utility.logger_application import get_logger_name
logger =get_logger_name(str(__file__).split('\\')[-1])



import csv


def read_file(filename):
    logger.info("read file function execution started")
    with open(filename) as fp:
        r = csv.reader(fp)
        data = list(r)
        logger.info("data reading completed")
    return data

def record_filter_it(data):
    it_records = []
    for row in data:
        if row[-1] == 'IT':
            it_records.append(row)
    logger.info("it records fetched")
    return it_records


def write_IT_records(header, it_records):
    with open("it_records.csv", "w", newline='') as fp:
        w = csv.writer(fp)
        w.writerow(header)
        w.writerows(it_records)
        logger.info("new file created :it_records.csv")

def main():
    logger.info("main function started...")
    filename = 'empsal_part_buck (2).csv'
    logger.info("{} file selected".format(filename))
    logger.info("reading file {}".format(filename))
    data = read_file(filename)
    logger.info("data read successfully")
    header = data[0]
    logger.info("headers are :{}".format(header))
    logger.info("record filtering started for IT reacords")
    IT_Records = record_filter_it(data)
    logger.info("IT Recored filtered")
    write_IT_records(header, IT_Records)
    logger.info("write operation successfully")
    logger.info("program completed")


if __name__ == '__main__':
    main()

