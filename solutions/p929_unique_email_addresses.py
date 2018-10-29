class Solution(object):
    def numUniqueEmails(self, emails):
        domains = {}
        for candidate in emails:
            local, domain = candidate.split('@')
            if domain not in domains:
                domains[domain] = [parse(local)]
            else:
                parsed = parse(local)
                if parsed not in domains[domain]:
                    domains[domain].append(parsed)
        counter = 0
        for domain in domains:
            counter += len(domains[domain])
        return counter
            
def parse(local):
    output = ''
    counter = 0
    dim = len(local)
    plus = False
    while counter < dim and not plus:
        char = local[counter]
        if char == '.':
            pass
        elif char == '+':
            plus = True
        else:
            output += char
        counter += 1
    return output
