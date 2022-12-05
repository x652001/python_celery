from workers.worker_main import add

class Web():
    def run(self):
        add.delay(8,3)


if __name__ == '__main__':
    app = Web()
    app.run()

