class Solution(object):
    def numUniqueEmails(self, emails):
        domains = []
        for candidate in emails:
            local, domain = candidate.split('@')
            parsed = parse(local)
            total = parsed + domain
            if total not in domains:
                domains.append(total)
        return len(domains)
            
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
