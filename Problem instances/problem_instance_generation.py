
import random
import time
import json
import pandas as pd

MIN_PROCESSING_TIME = 1
MAX_PROCESSING_TIME = 10
PROCESSING_TIME_STEPS = 1


def create_problem_instance(num_jobs, num_machines):
    # list for storing the (machine_id, processing_time) tuples
    problem_instance = []

    # create num_jobs number of jobs by assigning each all machines to the job in a random order
    # and assigning each machine job a random processing time of maximum MAX_PROCESSING_TIME
    for job in range(num_jobs):
        # list to keep track of the machines that have not been used yet for this job
        machines = list(range(num_machines))
        # store machine id and processing time tuples
        job_instance = []
        # add machines to job instance in random order with a random processing time fitting the min, max, and step size
        # as defined in the constants above
        for machine in range(num_machines):
            random.shuffle(machines)
            machine_and_time = (
            machines.pop(), (random.randint(MIN_PROCESSING_TIME, MAX_PROCESSING_TIME) * PROCESSING_TIME_STEPS))
            job_instance.append(machine_and_time)

        problem_instance.append(job_instance)

    return problem_instance



five_jobs_five_machines = create_problem_instance(6, 6)
print(five_jobs_five_machines)

num_jobs = list(range(5, 105, 5))  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
num_machines = list(range(5, 26, 1))  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

job_shop_data = []
for job_num in num_jobs:
    for machine_num in num_machines:
        start_time = time.time()
        instance_id = '{job}j{machine}m'.format(job=job_num, machine=machine_num)
        problem_instance = create_problem_instance(job_num, machine_num)
        job_shop_data.append((instance_id, job_num, machine_num, problem_instance))
        print("--- %s seconds ---" % (time.time() - start_time))

job_shop_df = pd.DataFrame(job_shop_data, columns=('instance_id', 'num_jobs', 'num_machines', 'problem_instance'))

job_shop_df.to_csv('job_shop_data.csv', sep=';', index=False)


