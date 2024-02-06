import random
import time
from TinderNav import TinderNav

# parameters
chance_to_like = .93
min_wait_time = .5
max_wait_time = 2
max_wait_for_like_button = 240


def main():
    err_count = 0

    tbot = TinderNav()
    tbot.createDriver()
    tbot.load_webpage()
    tbot.login()

    print('======== Running, use ctrl+c to quit  ========')

    try:
        while True:
            time.sleep(random.uniform(min_wait_time, max_wait_time))
            tbot.wait_for_like_button(max_wait_for_like_button)
            try:
                if random.random() < chance_to_like:
                    tbot.like()
                else:
                    tbot.dislike()

                err_count = 0
                
            except Exception:
                if err_count >= 2:
                    break
                else:
                    err_count += 1
                    tbot.load_webpage()

    except KeyboardInterrupt:
        pass
        
    input('\nsomething went wrong :( ... press enter to quit')
    tbot.quit()
        

if __name__ == "__main__":
    main()
