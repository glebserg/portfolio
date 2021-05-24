import socket
import threading
import argparse


"""

Сканирование доступных портов в сети

"""


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', type=str, help='Host. Example:"192.168.0.2/24"', metavar='')
parser.add_argument('-p', '--ports',type=int,nargs='+', help='Ports. Example: "80,433..."', metavar='')
args = parser.parse_args()


class PortScanner:

    list_ip = []
    list_result = []

    def __init__(self, input_ip, input_ports):
        self.input_ip = input_ip
        self.input_ports = input_ports

    def __make_list_ip(self, input_range):
        """
        Наполняем список ip-адресами для сканирования

        :param input_range:
        :return:
        """
        subnet = '.'.join(input_range.split('.')[:3])

        range_ip = input_range.split('.')[-1]
        start, finish = range_ip.split('/')

        for id_ip in range(int(start), int(finish) + 1):
            self.list_ip.append(f'{subnet}.{id_ip}')

    def __try_connect(self, ip, port_number):
        """
        Функция попытки соединения с портом

        :param ip:
        :param port_number:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1)
        try:
            sock.connect((ip, port_number))
            self.list_result.append(f'{ip} {port_number} OPEN')
        except:
            pass

    def __scan_ports(self, host_ip, list_port):
        """
        Запускаем и заканчиваем потоки для сканирования портов по конкретному ip-адресу

        :param host_ip:
        :param list_port:
        :return:
        """

        list_thread = []

        for port in list_port:
            thread = threading.Thread(target=self.__try_connect, args=(host_ip, port))
            list_thread.append(thread)

        for thread in list_thread:
            thread.start()

        for thread in list_thread:
            thread.join()

    def show_result(self):
        """
        Итерируемся по списку и выводим на консоль, если он не пуст

        :return:
        """
        if self.list_result:
            for result in self.list_result:
                print(result)
        else:
            print('No result')

    def run(self):
        """
        Запуск процесса сканирования

        :return:
        """
        self.__make_list_ip(input_range=self.input_ip)
        for ip_address in self.list_ip:
            self.__scan_ports(ip_address, self.input_ports)


if __name__ == "__main__":
    scan = PortScanner(input_ip=args.ip,
                       input_ports=args.ports)
    scan.run()
    scan.show_result()

# python port_scanner.py -i 217.69.128.10/50 -p 80 443
