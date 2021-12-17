def main():
    hexa_to_bits = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    packets = []
    bits = None 
    with open('input.txt', 'r') as file:
        hexa = file.readline()[:-1]
        temp = []
        for h in hexa:
            temp.append(hexa_to_bits[h])
        temp = [y for x in temp for y in x]
        bits = temp
    bits = "".join(bits)
    index = 0
    while index < len(bits)-1:
        temp = []
        index, temp = find_packets(index, bits, temp, "packet")
        packets.append(temp)
        if bits[index:].count('0') == len(bits[index:]):
            break
    # Packet = (Version, Packet Type, [Length Type], [Length], [Sub Packet, Number...])
    print(calculate_packet(packets[0]))

def calculate_packet(_packet):
    type_id = _packet[0][1]
    packet = _packet[0]
    if type_id == 0:
        n = 0
        for i in range(1, len(_packet)):
            n += calculate_packet(_packet[i])
        return n
    if type_id == 1:
        n = 1
        for i in range(1, len(_packet)):
            n *= calculate_packet(_packet[i])
        return n
    if type_id == 2:
        n = []
        for i in range(1, len(_packet)):
            n.append(calculate_packet(_packet[i]))
        return min(n)
    if type_id == 3:
        n = []
        for i in range(1, len(_packet)):
            n.append(calculate_packet(_packet[i]))
        return max(n)
    if type_id == 4:
        return packet[2]
    if type_id == 5:
        n = []
        for i in range(1, len(_packet)):
            n.append(calculate_packet(_packet[i]))
        return 1 if n[0] > n[1] else 0
    if type_id == 6:
        n = []
        for i in range(1, len(_packet)):
            n.append(calculate_packet(_packet[i]))
        return 1 if n[0] < n[1] else 0
    if type_id == 7:
        n = []
        for i in range(1, len(_packet)):
            n.append(calculate_packet(_packet[i]))
        return 1 if n[0] == n[1] else 0

def find_packets(index, bits, sub_packets, p):
    version = int(bits[index:index+3],2)
    packet_type = int(bits[index+3:index+6], 2)
    if packet_type != 4:
        length_type = bits[index+6:index+7]
        if int(length_type) == 1:
            length_subpackets = int(bits[index+7:index+18], 2)
            index += 18
            sub_packets.append((version, packet_type, int(length_type), length_subpackets, p))
            while len(sub_packets) <= length_subpackets:
                index, temp = find_packets(index, bits, [], "sub packet")
                sub_packets.append(temp)
            return index, sub_packets 
        else:
            length_subpackets_bits = int(bits[index+7:index+22], 2)
            index += 22
            sub_packets.append((version, packet_type, int(length_type), length_subpackets_bits, p))
            packet_end = length_subpackets_bits + index
            while index < packet_end:
                index, temp = find_packets(index, bits, [], "sub packet")
                sub_packets.append(temp)
            return index, sub_packets
    else:
        n_bits = 6
        index += 6
        temp = bits[index:index+5]
        n_bits += 5
        number = ""
        while temp[0] != '0':
            number += temp[1:]
            index += 5
            n_bits += 5
            temp = bits[index:index+5]
        number += temp[1:]
        index += 5
        n_bits += 5
        number = int(number, 2)
        sub_packets.append((version, packet_type, number))
        return index, sub_packets
    
main()
