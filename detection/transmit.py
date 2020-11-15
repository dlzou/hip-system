from collections import deque

def transmitter(buffer_len=50, threshold=0.8):
    buffer = deque([0 for _ in range(buffer_len)])

    def transmit_next(hit):
        assert hit == 0 or hit == 1, "argument must be binary"
        nonlocal buffer
        buffer.pop()
        buffer.appendleft(hit)
        if sum(buffer) / buffer_len > threshold:
            emit()
            buffer = deque([0 for _ in range(buffer_len)])

    return transmit_next


def emit():
    print("Save that baby!") # hook this to hip-system hardware
