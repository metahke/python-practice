import random
import datetime
import threading
from multiprocessing import Pool


def generate_hundred_nums_list():
    return [random.randrange(0, 100) for num in range(100)]


def sort_nums_list(num_list):
    for left_index in range(len(num_list)):
        for right_index in range(left_index + 1, len(num_list)):
            left_num, right_num = num_list[left_index], num_list[right_index]

            if left_num > right_num:
                num_list[left_index], num_list[right_index] = num_list[right_index], num_list[left_index]

    return num_list


def calc_time_exec(func):
    def wrapper(*args, **kwargs):
        time_before = datetime.datetime.now()

        func(*args, **kwargs)

        time_after = datetime.datetime.now()

        print(f"{func.__name__}: {time_after - time_before}")

    return wrapper


@calc_time_exec
def one_thread_solution(nums_list):
    for hundred_num_list in nums_list[:]:
        sort_nums_list(hundred_num_list)


@calc_time_exec
def threading_solution(nums_list):
    threads = [threading.Thread(target=sort_nums_list, args=[hundred_num_list])
               for hundred_num_list in nums_list]

    for thread in threads:
        thread.start()
        thread.join()


@calc_time_exec
def multiprocessing_solution(nums_list):
    pool = Pool(processes=10)

    pools = [pool.apply_async(sort_nums_list, [hundred_num_list])
             for hundred_num_list in nums_list]

    pool.close()
    pool.join()


def main():
    ten_hundred_nums_lists = [generate_hundred_nums_list() for i in range(10)]

    # one thread solution
    one_thread_solution(ten_hundred_nums_lists[:])

    # threading
    threading_solution(ten_hundred_nums_lists[:])

    # multiprocessing
    multiprocessing_solution(ten_hundred_nums_lists[:])

    """
    Ile wątków należy stworzyć, aby program był wykonany jak najszybciej i 
    optymalnie? Aby odpowiedzieć na to pytanie, zapoznaj się z “Amdahl’s Law”.
    
    > Myślę, że... by program był wykonywany jak najszybciej i najbardziej optymalnie,
    to im większa liczba wątków, tym lepiej? W rzeczywistości można to obliczyć według wzoru i zależne jest to od tego,
    jaka część danego programu może być ulepszona.
    No i zapewne najlepiej byłoby sprawdzać to ręcznie, czyli zwiększać liczbę wątków i sprawdzać efekt
    indywidualnie na danej maszynie i programie.
    
    ???
    """


if __name__ == "__main__":
    main()
