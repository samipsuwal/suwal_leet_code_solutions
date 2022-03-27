class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        
        def killAllChildren(kill, parentToChild, spree):
            if kill in parentToChild:
                for child in parentToChild[kill]:
                    spree.append(child)
                    killAllChildren(child, parentToChild, spree)
            
            return spree
        
        parentToChild = {}
        
        #construct parent to child tree
        for i, parent in enumerate (ppid):
            if parent not in parentToChild:
                parentToChild[parent] = [pid[i]]
            else:
                parentToChild[parent].append(pid[i])

            
        spree = [kill]
        
        print(parentToChild)
        
        killAllChildren(kill, parentToChild, spree)
            
            
        return spree
            