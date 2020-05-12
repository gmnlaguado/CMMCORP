# coding=utf-8
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from functools import partial
from threading import Thread
from random import random


class TestApp(App):
    def save_result(self, name, result, dt):
        # This function executes in the UI thread, called once for each result
        # The order in which the results are returned is non-deterministic.
        # DO SOMTHING WITH result HERE
        self.button.text += 'Thread \'' + name + '\' finished, value = ' + \
                            str(result) + '\n'
        # All done?
        self.num_results += 1
        if self.num_results == len(self.task_names):
            self.button.text += '\nNotice the order is non-deterministic\n'
            self.running = False
            self.button.text += '\nTap to Start Threads Again'

    def generate_pseudo_random_prime(self):
        # A task that is slow-ish, make it slower by increasing MAX
        MAX = 40000
        last = 0
        for num in range(1, round(MAX * random())):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                last = num
        return last

    def do_task(self, name):
        # This function executes in its own thread
        # DO COMPUTE INTENSIVE TASK OR INTERNET ACCESS HERE, AND GET A result
        # DO NOT write to UI
        result = self.generate_pseudo_random_prime()
        # Sync this thread's result with Kivy UI thread
        Clock.schedule_once(partial(self.save_result, name, result), 0)

    def start_threads(self):
        if not self.running:
            self.running = True
            self.num_results = 0
            self.task_names = ['a', 'b', 'c', 'd', 'e', 'f']
            # Uses multiple cores on Android, but 1 core on Desktop
            for name in self.task_names:
                Thread(target=self.do_task, args=(name), daemon=True).start()
            self.button.text = 'Started 6 threads\n\n'

    def build(self):
        self.running = False
        self.button = Button(text='Tap to Start Threads')
        self.button.on_release = self.start_threads
        return (self.button)


if __name__ == '__main__':
    TestApp().run()