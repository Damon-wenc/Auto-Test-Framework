import webbrowser

webbrowser.open_new_tab('localhost:8888')

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
