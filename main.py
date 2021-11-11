from application import data, parsing

if __name__ == '__main__':
    raw_data_path = 'data/phonebook_raw.csv'
    raw_contact_list = data.get_raw(raw_data_path)

    contact_list_with_doubles = parsing.read_raw_data(raw_contact_list)
    true_contact_list = parsing.true_contact_list(contact_list_with_doubles)

    true_data_path = 'data/phonebook_true.csv'
    data.save_true(true_contact_list, true_data_path)
