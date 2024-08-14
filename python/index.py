import schedule
import time

def job():
    print("Hello World")

def main():
    print("I'm working...")
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()