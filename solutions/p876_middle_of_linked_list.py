class Solution(object):
    def middleNode(self, head):
        newlist = [head.val]
        counter = 1
        while head.next != None:
            counter += 1
            head = head.next
            newlist.append(head.val)
        return newlist[counter/2:]
