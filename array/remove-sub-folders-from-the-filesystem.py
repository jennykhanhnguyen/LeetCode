class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """

        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)
        return res
