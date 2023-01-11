import struct
import socket


def calculate_broadcast_address(ip_address: str, subnet_mask: str) -> str:
    # Convert IP address and subnet mask to integers
    try:
        ip_int = struct.unpack("!I", socket.inet_aton(ip_address))[0]
        mask_int = struct.unpack("!I", socket.inet_aton(subnet_mask))[0]
    except ValueError:
        return "Invalid IP address or subnet mask"

    # Calculate the broadcast address by performing a bitwise OR operation
    # on the inverted subnet mask and the IP address
    broadcast_int = ip_int | ~mask_int

    # Convert the broadcast address to a string using a list comprehension
    broadcast_address = ".".join([str((broadcast_int >> (8 * (3 - i))) & 0xff) for i in range(4)])

    return broadcast_address


def main():
    while True:
        ip_address = input("Enter an IP address: ")
        subnet_mask = input("Enter a subnet mask: ")

        broadcast_address = calculate_broadcast_address(ip_address, subnet_mask)
        print(f"Broadcast address: {broadcast_address}")


main()
