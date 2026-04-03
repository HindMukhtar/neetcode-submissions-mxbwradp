class Twitter:

    def __init__(self):
        self.time = 0 
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1 
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        tweet_heap = []
        for u in users: 
            tweet_idx = len(self.tweets[u])-1
            if tweet_idx >= 0: 
                time, tweet = self.tweets[u][tweet_idx]
                tweet_heap.append((time, tweet, u, tweet_idx))

        heapq.heapify(tweet_heap)
        res = []

        while len(res) < 10 and tweet_heap: 
            time, tweet, u, tweet_idx = heapq.heappop(tweet_heap) 
            res.append(tweet)
            if tweet_idx-1 >= 0: 
                time, tweet = self.tweets[u][tweet_idx-1]
                heapq.heappush(tweet_heap, (time, tweet, u, tweet_idx-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]: 
            self.following[followerId].remove(followeeId)
        
