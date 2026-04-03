class Twitter:

    def __init__(self):
        self.tweet_counter = 0 
        self.following = defaultdict(set)
        self.tweets = [] 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_counter+=1 
        self.tweets.append((-self.tweet_counter, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_heap = [(time, tweet) for time, tweet, u in self.tweets if u == userId or u in self.following[userId]]
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
        
