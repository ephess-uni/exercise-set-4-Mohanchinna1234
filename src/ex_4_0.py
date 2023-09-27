""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    with open('logfile','r') as file:
        lst = []
        ans = []
        ans1 = []
        for i in file:
            j = i.strip().split()
            lst.append(j)
        for i in range(0,len(lst)):
            if len(lst[i]) > 1:
                if lst[i][-1] == 'initiated.' and lst[i][-2] == 'Shutdown':
                    ans.append(lst[i])
    if len(ans) < 1:
        return []
    else:
        for i in ans:
            i = ','.join(i)
            ans1.append(i)
        return ans1


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
