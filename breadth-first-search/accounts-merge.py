from collections import defaultdict, deque

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = defaultdict(set)
        email_to_name = {}

        # 1) Build the graph
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]

            # Record name for each email
            for e in emails:
                email_to_name[e] = name

            # Connect all emails in this account together
            first = emails[0]
            for e in emails[1:]:
                graph[first].add(e)
                graph[e].add(first)

            if first not in graph:
                graph[first] = set()


        # 2) BFS to find connected components of emails
        visited = set()
        res = []

        for email in graph:
            if email in visited:
                continue

            # Start BFS for this component
            q = deque([email])
            visited.add(email)
            component_emails = []

            while q:
                cur = q.popleft()
                component_emails.append(cur)

                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            # 3) Format output: [name] + sorted emails
            component_emails.sort()
            name = email_to_name[email]  # any email in component works
            res.append([name] + component_emails)

        return res
