class Twitter:

    def __init__(self):
        self.tweet_counter = 0 
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_counter+=1 
        self.tweets[userId].append((-self.tweet_counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        tweet_heap = []
        for u in users: 
            tweet_heap.extend(self.tweets[u])
        heapq.heapify(tweet_heap)
        count = 0 
        res = []
        while count < 10 and tweet_heap: 
            _, tweet_id = heapq.heappop(tweet_heap) 
            res.append(tweet_id)
            count += 1 

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]: 
            self.following[followerId].remove(followeeId)
        
