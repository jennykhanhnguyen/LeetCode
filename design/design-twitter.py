from collections import defaultdict
import heapq
class Twitter:

    class TwitterUser:
        def __init__(self, userId):
            self.following = set()
            self.posts = list()

    def __init__(self):
        self.id_to_object = dict()
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.id_to_object:
            new_account = self.TwitterUser(userId)
            self.id_to_object[userId] = new_account
        account = self.id_to_object[userId]
        self.order += 1
        account.posts.append((self.order, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.id_to_object:
            new_account = self.TwitterUser(userId)
            self.id_to_object[userId] = new_account
        account = self.id_to_object[userId]
        followees = set(account.following)
        followees.add(userId)
        heap = []
        to_break = {acc: False for acc in followees} # id
        index = {acc: -1 for acc in followees} # id
        while not all(to_break.values()):
            for following_id in followees:
                if to_break[following_id] == True:
                    continue
                following_account = self.id_to_object.get(following_id)

                if not following_account:
                    to_break[following_id] = True
                    continue
                if len(following_account.posts) == 0 or abs(index[following_id]) > len(following_account.posts):
                    to_break[following_id] = True
                    continue
                weight, post_id = following_account.posts[index[following_id]]

                if to_break[following_id] == True:
                    continue
                heapq.heappush(heap, (-1*weight, post_id))
                index[following_id] -= 1
        ans = []
        for i in range(min(10, len(heap))):
            top_weight, top_post = heapq.heappop(heap)
            ans.append(top_post)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id_to_object:
            new_account = self.TwitterUser(followerId)
            self.id_to_object[followerId] = new_account
        account = self.id_to_object[followerId]
        
        if followeeId not in account.following:
            account.following.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id_to_object:
            new_account = self.TwitterUser(followerId)
            self.id_to_object[followerId] = new_account
        account = self.id_to_object[followerId]
        
        if followeeId in account.following:
            account.following.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)