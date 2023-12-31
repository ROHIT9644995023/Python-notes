from csv import DictWriter
with open('final.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow,writerows
    # csv_writer.writerow({
    #     'firstname':'rohit',
    #     'lastname':'tanwar',
    #     'age':500
    # })
    # csv_writer.writerow({
    #     'firstname':'mohit',
    #     'lastname':'tanwar',
    #     'age':500
    # })

    # writerows --> [dict, dict, dict] 
    csv_writer.writerows([
        {'firstname':'rohit','lastname':'tanwar','age':200},
        {'firstname':'rohit','lastname':'tanwar','age':200},
        {'firstname':'rohit','lastname':'tanwar','age':200},
    ])