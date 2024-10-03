def receive_frames():
    sender_buffer = "Sender_Buffer.txt"
    receiver_buffer = "Receiver_Buffer.txt"
    expected_frame = 0

    while True:
        if os.path.exists(sender_buffer):
            with open(sender_buffer, "r") as f:
                frames = f.readlines()

            for frame in frames:
                frame_number = int(frame.split()[1][:-1])  # Extract the frame number
                data = frame.split(":")[1].strip()

                print(f"Received Frame {frame_number}: {data}")

                if random.random() < 0.2:
                    print(f"Simulating error for Frame {frame_number}")
                    ack_message = f"NACK {frame_number}"
                elif frame_number == expected_frame:
                    print(f"Frame {frame_number} is as expected.")
                    ack_message = f"ACK {frame_number}"
                    expected_frame += 1
                else:
                    print(f"Frame {frame_number} is not as expected. Expected Frame {expected_frame}.")
                    ack_message = f"NACK {expected_frame}"

                with open(receiver_buffer, "w") as f:
                    f.write(ack_message)

                time.sleep(1)

            os.remove(sender_buffer)
        else:
            time.sleep(0.5)
receive_frames()
