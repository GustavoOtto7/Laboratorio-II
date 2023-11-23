def check_ip_is_valid(ip):
    try:
        nums = ip.split('.')
        if len(nums) != 4:
            return False
        for index, num in enumerate(nums):
            if index == 0:
                assert int(num) >= 1 and int(num) <= 255
            else:
                assert int(num) >= 0 and int(num) <= 255
        return True
    except BaseException:
        return False


def verify_ips():
    ips_file = open("Laboratorio-II/Semana_10/ips.txt")
    valid_ips = []
    invalid_ips = []
    for ip in ips_file:
        is_valid = check_ip_is_valid(ip)
        if is_valid == True:
            valid_ips.append(ip)
        else:
            invalid_ips.append(ip)
        print("Válidos: ", valid_ips)
        print("Inválidos: ", invalid_ips)
    valid_ips_file = open("Laboratorio-II/Semana_10/valid_ips.txt", "w")
    invalid_ips_file = open("Laboratorio-II/Semana_10/invalid_ips.txt", "w")
    valid_ips_file.writelines(valid_ips)
    invalid_ips_file.writelines(invalid_ips)
    valid_ips_file.close()
    invalid_ips_file.close()

def main():
    ip = verify_ips()
    check_ip_is_valid(ip)

main()