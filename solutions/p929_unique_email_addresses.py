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
    dim = len(local)
    counter = 0
    while counter < dim:
        char = local[counter]
        if char == '+':
            return local[:counter]
        elif char == '.':
            local = local[:counter] + local[counter+1:]
        counter += 1
    return local
