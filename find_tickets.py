#!/usr/bin/python2.7

# Please don't just copy the code, lmao.

def find_numbers(string_list):
    lottery_numbers = []

    for ticket_number in string_list:
        if len(ticket_number) >= 7 and len(ticket_number) <= 14:
            temp_result = {}
            final_result = []
            n_double = len(ticket_number) - 7
            n_single = 7 - n_double
            is_valid_ticket(final_result, temp_result, ticket_number, n_double, n_single, 0)

            if final_result:
                lottery_numbers.append(final_result)

    return lottery_numbers

def is_valid_ticket(final_result, temp_result, ticket_number, n_double, n_single, index):
    if (index >= len(ticket_number) or (n_double == 0 and n_single == 0)):
        return final_result

    if n_double > 0:
        cur_digit = ticket_number[index:index + 2]

        if int(cur_digit) < 60 and cur_digit not in temp_result:
            temp_result[cur_digit] = None
            valid_number = is_valid_ticket(final_result, temp_result, ticket_number, n_double - 1, n_single, index + 2)

            if valid_number is not None:
                final_result.append(cur_digit)
                return valid_number

    if n_single > 0:
        cur_digit = ticket_number[index]

        if cur_digit != '0' and cur_digit not in temp_result:
            temp_result[cur_digit] = None
            valid_number = is_valid_ticket(final_result, temp_result, ticket_number, n_double, n_single - 1, index + 1)

            if valid_number is not None:
                final_result.append(cur_digit)
                return valid_number

    return None
     

if __name__ == '__main__':
    # Only the first 6 numbers are supposed to be valid lottery tickets for Morty.
    # 12141516171819 => 12 14 15 16 17 18 19
    # 1123566229 => 11 2 3 56 6  22 9
    # 4938532894754 => 49 38 53 28 9 47 53
    # 1234567 => 1 2 3 4 5 6 7
    # 11123456 => 11 1 2 3 4 5 6
    # 1223345456591 => 12 23 34 54 56 59 1
    candidates = ['12141516171819', '1123566229', '4938532894754', '1234567', '11123456', '1223345456591',
                  '0', '000000000', '111111111111', '64123456', '569815571556', '472844278465445'
                  '1213456', '1263345456621', '471298347289174289378923718', '1234507', '', '22223334454647']

    lottery_numbers = find_numbers(candidates)

    if len(lottery_numbers) > 0:
        print 'Morty, here are your lottery tickets for today:\n'

        for number in lottery_numbers:
            print '%s => %s' % (''.join(reversed(number)).ljust(14), ' '.join(reversed(number)))
    else:
        print 'No lottery tickets found :('
