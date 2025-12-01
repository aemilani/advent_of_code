import numpy as np


def rule_holds(r1, r2, update):
    if (r1 in update) and (r2 in update):
        if update.index(r1) < update.index(r2):
            return True
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    with open('../../data/2024/05.txt', 'r') as f:
        string = f.read().strip()

    rules = string.split('\n\n')[0].split('\n')
    updates = string.split('\n\n')[1].split('\n')

    for i in range(len(rules)):
        rules[i] = rules[i].split('|')
    for i in range(len(updates)):
        updates[i] = updates[i].split(',')

    sum_mids = 0
    for update in updates:
        n_true_rules = 0
        for rule in rules:
            if rule_holds(rule[0], rule[1], update):
                n_true_rules += 1
        if n_true_rules == len(rules):
            sum_mids += int(update[int(len(update) / 2)])

    print(f'Part 1: {sum_mids}')

    sum_mids = 0
    for update in updates:
        corrected = False
        incorrect = False
        for rule in rules:
            if not rule_holds(rule[0], rule[1], update):
                incorrect = True
        while incorrect:
            for rule in rules:
                if not rule_holds(rule[0], rule[1], update):
                    r1, r2 = rule[0], rule[1]
                    r1_idx, r2_idx = update.index(r1), update.index(r2)
                    update[r1_idx] = r2
                    update[r2_idx] = r1
                    corrected = True
            n_true_rules = 0
            for rule in rules:
                if rule_holds(rule[0], rule[1], update):
                    n_true_rules += 1
            if n_true_rules == len(rules):
                incorrect = False
        if corrected:
            sum_mids += int(update[int(len(update) / 2)])

    print(f'Part 2: {sum_mids}')
