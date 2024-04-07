def find_least_common_packet(device, packets_to_send):
    min_count = float('inf')
    least_common_packet = None
    for packet_id, packet in enumerate(packets_to_send):
        if packet_id not in device['downloads']:
            if len(packet) < min_count:
                min_count = len(packet)
                least_common_packet = packet_id
            elif len(packet) == min_count and least_common_packet > packet_id:
                least_common_packet = packet_id
    return least_common_packet


def find_device_to_request_from(devices, packets_to_send, least_common_packet_id):
    min_download = float('inf')
    device_to_request_from = None
    for device_id in packets_to_send[least_common_packet_id]:
        device = devices[device_id]
        if len(device['downloads']) < min_download:
            min_download = len(device['downloads'])
            device_to_request_from = device
        elif len(device['downloads']) == min_download and len(device_to_request_from['downloads']) > len(device['downloads']):
            min_download = len(device['downloads'])
            device_to_request_from = device
        elif len(device['downloads']) == min_download and len(device_to_request_from['downloads']) == len(device['downloads']) and device_to_request_from['device_id'] > device_id:
            min_download = len(device['downloads'])
            device_to_request_from = device
    return device_to_request_from


def select_valid_request(devices, pending_requests):
    max_worth = -float('inf')
    selected_request = None
    for req in pending_requests:
        worth = devices[req['send_to']['device_id']]['worth']
        if worth[req['from']['device_id']] > max_worth:
            selected_request = req
            max_worth = worth[req['from']['device_id']]
        elif worth[req['from']['device_id']] == max_worth and len(req['from']['downloads']) == len(selected_request['from']['downloads']) and selected_request['from']['device_id'] > req['from']['device_id']:
            selected_request = req
            max_worth = worth[req['from']['device_id']]
        elif worth[req['from']['device_id']] == max_worth and len(req['from']['downloads']) < len(selected_request['from']['downloads']):
            selected_request = req
            max_worth = worth[req['from']['device_id']]
    return selected_request


def generate_requests(devices, packets_to_send, requests):
    for device in devices.values():
        if device['device_id'] != 0:
            least_common_packet_id = find_least_common_packet(device, packets_to_send)
            if least_common_packet_id is None:
                continue
            device_to_request_from = find_device_to_request_from(devices, packets_to_send, least_common_packet_id)
            new_request = {
                'from': device,
                'send_to': device_to_request_from,
                'packet_id': least_common_packet_id,
            }
            requests[device_to_request_from['device_id']].append(new_request)


def respond_to_requests(devices, packets_to_send, requests):
    valid_requests = []
    for device_id, pending_requests in requests.items():
        if pending_requests:
            valid_request = select_valid_request(devices, pending_requests)
            valid_requests.append(valid_request)

    for valid_request in valid_requests:
        devices[valid_request['from']['device_id']]['worth'][valid_request['send_to']['device_id']] += 1
        devices[valid_request['from']['device_id']]['downloads'].add(valid_request['packet_id'])
        packets_to_send[valid_request['packet_id']].add(valid_request['from']['device_id'])


def update_result(devices, packets_to_send, result):
    for device in devices.values():
        if len(device['downloads']) != len(packets_to_send):
            result[device['device_id']] += 1


def solve():
    n, k = map(int, input().split())
    devices = {
        i: {
            'downloads': set(range(k)) if i == 0 else set(),
            'device_id': i,
            'worth': {j: 0 for j in range(n) if j != i},
        }
        for i in range(n)
    }
    packets_to_send = [{0} for _ in range(k)]
    result = [0 for _ in range(n)]

    while any(len(packet) != n for packet in packets_to_send):
        requests = {i: [] for i in range(n)}
        update_result(devices, packets_to_send, result)
        generate_requests(devices, packets_to_send, requests)
        respond_to_requests(devices, packets_to_send, requests)

    print(*result[1:])
    return


solve()
