import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", required=True, help="Path to people names to assign tasks")
    parser.add_argument("-t", required=True, help="Path to tasks")
    parser.add_argument("-o", required=True, help="Path to save task assignment")

    args = parser.parse_args()
    
    with open(args.p) as people_file:
        with open(args.t) as tasks_file:
            people = [line.strip() for line in people_file.readlines()]
            tasks = [line.strip() for line in tasks_file]
            assert len(people) == len(tasks), "The number of people does not much number of tasks, {} vs {}".format(len(people), len(tasks))

            np.random.shuffle(people)
            np.random.shuffle(tasks)
            print("")
            with open(args.o, "w+") as output_file:
                for i in range(len(people)):
                    out_str = "'{}' is assigned to task '{}' \n".format(people[i], tasks[i])
                    output_file.write(out_str)
                    print(out_str.strip())

            print()
if __name__ == "__main__":
    main()
