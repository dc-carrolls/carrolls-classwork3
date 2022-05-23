from datetime import datetime
import asyncore
from smtpd import SMTPServer

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = 'mail%s-%d.txt' %(datetime.now().strftime('%Y%m%d%H%M%S'),self.no)
        f = open(filename, 'w')
        f.write(mailfrom+'\n')
        for address in rcpttos:
            f.write(address+'\n')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.no += 1


def main():
    # start the smtp server on xxx.xxx.xxx.xxx:1025
    foo = EmlServer(('192.168.0.227', 1025),('localhost', 1025), map=None, decode_data=True)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
