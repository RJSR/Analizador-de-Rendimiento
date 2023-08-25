def mm1_queue_performance(arrival_rate, service_rate):
    utilization = arrival_rate / service_rate
    avg_queue_length = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
    avg_wait_queue = avg_queue_length / arrival_rate
    avg_system_length = arrival_rate / (service_rate - arrival_rate)
    avg_wait_system = avg_system_length / arrival_rate
    
    return utilization, avg_queue_length, avg_wait_queue, avg_system_length, avg_wait_system

arrival_rate = 10  # requests per second
service_rate = 1 / 0.08  # requests per second

utilization, avg_queue_length, avg_wait_queue, avg_system_length, avg_wait_system = mm1_queue_performance(arrival_rate, service_rate)

print(f"Utilization: {utilization:.2f}")
print(f"Avg Queue Length: {avg_queue_length:.2f}")
print(f"Avg Wait in Queue: {avg_wait_queue:.2f} seconds")
print(f"Avg System Length: {avg_system_length:.2f}")
print(f"Avg Wait in System: {avg_wait_system:.2f} seconds")
