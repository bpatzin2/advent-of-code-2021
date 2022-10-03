literal_test_data = """
D2FE28
""".strip()

operator_test_data0 = """
38006F45291200
""".strip()
operator_test_data0a = """
EE00D40C823060
""".strip()

operator_test_data1 = """
8A004A801A8002F478
""".strip()
operator_test_data2 = """
620080001611562C8802118E34
""".strip()
operator_test_data3 = """
C0015000016115A2E0802F182340
""".strip()
operator_test_data4 = """
A0016C880162017C3686B18A3D4780
""".strip()


def parse_input(lines):
    result = ""
    for c in lines[0]:
        r = "{0:04b}".format(int(c, 16))
        result += r
    return result


def decode_literal(remaining_packet):
    result = ""
    group = remaining_packet[:5]
    result += group[1:5]
    remaining_packet = remaining_packet[5:]
    while group[0] != "0":
        group = remaining_packet[:5]
        remaining_packet = remaining_packet[5:]
        result += group[1:5]
    return int(result, 2), remaining_packet


def decode_operator(remaining_packet):
    len_type_id = remaining_packet[0]
    remaining_packet = remaining_packet[1:]
    result = []
    if len_type_id == "0":
        total_sub_packet_len_b = remaining_packet[:15]
        remaining_packet = remaining_packet[15:]
        total_sub_packet_len = int(total_sub_packet_len_b, 2)
        processed_bits = 0
        while processed_bits < total_sub_packet_len:
            tree = decode(remaining_packet)
            result.append(tree)
            processed_bits += len(remaining_packet) - len(tree["remaining_packet"])
            remaining_packet = tree["remaining_packet"]
    else:
        num_sub_packets_b = remaining_packet[:11]
        remaining_packet = remaining_packet[11:]
        num_sub_packets = int(num_sub_packets_b, 2)
        while num_sub_packets > 0:
            tree = decode(remaining_packet)
            result.append(tree)
            remaining_packet = tree["remaining_packet"]
            num_sub_packets -= 1
    return result, remaining_packet


def decode(packet_str):
    version_b = packet_str[:3]
    type_b = packet_str[3:6]
    if type_b == "100":
        literal_int, remaining_packet = decode_literal(packet_str[6:])
        return {
            "type_b": type_b,
            "type": int(type_b, 2),
            "version": int(version_b, 2),
            "literal": literal_int,
            "children": [],
            "remaining_packet": remaining_packet,
        }
    else:
        children, remaining_packet = decode_operator(packet_str[6:])
        return {
            "type_b": type_b,
            "type": int(type_b, 2),
            "version": int(version_b, 2),
            "literal": None,
            "children": children,
            "remaining_packet": remaining_packet,
        }


def eval_packet_tree(packet_tree):
    if packet_tree["literal"] is not None:
        return packet_tree["literal"]

    children = packet_tree["children"]
    type = packet_tree["type"]
    result = 0

    if type == 0:
        for child in children:
            r = eval_packet_tree(child)
            result += r
    elif type == 1:
        result = 1
        for child in children:
            result *= eval_packet_tree(child)
    elif type == 2:
        result = min(list(map(eval_packet_tree, children)))
    elif type == 3:
        result = max(list(map(eval_packet_tree, children)))
    elif type == 5:
        child1 = children[0]
        child2 = children[1]
        result = 1 if eval_packet_tree(child1) > eval_packet_tree(child2) else 0
    elif type == 6:
        child1 = children[0]
        child2 = children[1]
        result = 1 if eval_packet_tree(child1) < eval_packet_tree(child2) else 0
    elif type == 7:
        child1 = children[0]
        child2 = children[1]
        result = 1 if eval_packet_tree(child1) == eval_packet_tree(child2) else 0
    else:
        raise Exception("unknown type", type)
    return result


file = open("day16-input.txt", "r")
lines = file.read().splitlines()
operator_binary = parse_input(lines)
# literal_binary = parse_input(literal_test_data.split("\n"))
# operator_binary = parse_input(operator_test_data4.split("\n"))

# print(literal_binary)
# print(operator_binary)


# print(decode(literal_binary))
packet_tree = decode(operator_binary)
print(packet_tree)

r = eval_packet_tree(packet_tree)
print(r)
