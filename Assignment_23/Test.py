import threading
from queue import Queue

def compute_sum(numbers, result_queue):
    """Calculates the sum of elements and puts it in the queue."""
    total_sum = sum(numbers)
    result_queue.put(("Sum", total_sum))

def compute_product(numbers, result_queue):
    """Calculates the product of elements and puts it in the queue."""
    total_product = 1
    for num in numbers:
        total_product *= num
    result_queue.put(("Product", total_product))

def main():
    # Sample list of elements
    numbers = [2, 3, 4, 5]
    print(f"Input List: {numbers}\n")

    # Queue to collect results from threads
    result_queue = Queue()

    # Create Thread 1 for Sum and Thread 2 for Product
    thread1 = threading.Thread(target=compute_sum, args=(numbers, result_queue))
    thread2 = threading.Thread(target=compute_product, args=(numbers, result_queue))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish execution
    thread1.join()
    thread2.join()

    # Retrieve and display results from the main thread
    results = {}
    while not result_queue.empty():
        label, value = result_queue.get()
        results[label] = value

    print(f"Result from Thread 1: {results['Sum']}")
    print(f"Result from Thread 2: {results['Product']}")

if __name__ == "__main__":
    main()
