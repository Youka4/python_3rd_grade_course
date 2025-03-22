import multiprocessing
import time
import codecs


def process_a(queue_a, queue_b):
    while True:
        message = queue_a.get()
        if message == "STOP":
            break
        modified_message = message.lower()
        time.sleep(5)
        queue_b.put(modified_message)


def process_b(queue_b, queue_main):
    while True:
        message = queue_b.get()
        if message == "STOP":
            break
        encoded_message = codecs.encode(message, 'rot_13')
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print(f"[{current_time}] Process B: {encoded_message}")
        queue_main.put(encoded_message)


def main():
    input_queue_a = multiprocessing.Queue()
    output_queue_b = multiprocessing.Queue()
    output_queue_main = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(target=process_a, args=(input_queue_a, output_queue_b))
    process_b_instance = multiprocessing.Process(target=process_b, args=(output_queue_b, output_queue_main))

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            message = input()
            if message.lower() == "exit":
                input_queue_a.put("STOP")
                output_queue_b.put("STOP")
                break
            input_queue_a.put(message)
            start_time = time.time()

            result = output_queue_main.get()

            print(f"Final encoded message: {result}")
            print(f"Time taken for the process: {time.time() - start_time} seconds")
    except KeyboardInterrupt:
        pass
    process_a_instance.join()
    process_b_instance.join()

if __name__ == "__main__":
    main()
