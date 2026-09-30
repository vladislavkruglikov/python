def _recieve(socket) -> int:
    buffer = bytearray()
    while b"\n" not in buffer:
        chunk = socket.recv(1024)
        if chunk == b"":
            raise ConnectionError("Client closed before completing the message")
        buffer.extend(chunk)
    
    message, _, remaining = buffer.partition(b"\n")
    number = int(message.decode("utf-8"))
    return number
