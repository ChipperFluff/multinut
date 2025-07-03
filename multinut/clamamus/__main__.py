import argparse
import socket
from .server import *

def valid_port(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 65535:
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535.")
    return ivalue


def valid_host(value):
    try:
        socket.getaddrinfo(value, None)
    except socket.gaierror:
        raise argparse.ArgumentTypeError(f"Host '{value}' is not resolvable.")
    return value


def parse_args():
    parser = argparse.ArgumentParser(
        prog="clamamus",
        description="🗣️ Start the Clamamus server — where logs scream back."
    )

    parser.add_argument(
        "-p", "--port",
        type=valid_port,
        default=6969,
        metavar="PORT",
        help="TCP port to listen on (1–65535, default: 6969)"
    )

    parser.add_argument(
        "-H", "--host",
        type=valid_host,
        default="127.0.0.1",
        metavar="HOST",
        help="Resolvable host or IP address to bind to (default: 127.0.0.1)"
    )

    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress startup banners and non-log output"
    )

    parser.add_argument(
        "--max-clients",
        type=int,
        default=8,
        metavar="N",
        help="Maximum number of simultaneous clients (default: 8)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.quiet:
        print("🚀 Clamamus server initializing...")
        print(f"📡 Listening on {args.host}:{args.port}")
        print(f"🔢 Max clients allowed: {args.max_clients}")

    # --- Server startup placeholder ---
    print("💤 [dev] Server logic not implemented yet.")
    # future: start_clamamus_server(
    #     host=args.host,
    #     port=args.port,
    #     quiet=args.quiet,
    #     max_clients=args.max_clients
    # )


if __name__ == "__main__":
    main()
