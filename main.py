import GUI


def main():  # run mainloop
    root = GUI.Tk()
    app = GUI.MainApplication(root)
    root.title('Calculator')
    root.mainloop()


if __name__ == '__main__':
    main()

