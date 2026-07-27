class Twitter:

    def __init__(self):
        self.twin = dict()
        self.tweet = dict()
        self.nums = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.nums += 1
        if userId not in self.tweet:
            self.tweet[userId] = deque()

        if userId not in self.twin:
            self.twin[userId] = set()
            self.twin[userId].add(userId)

        if len(self.tweet[userId]) >= 10:
            self.tweet[userId].popleft()
        self.tweet[userId].append([- self.nums, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        news = list()
        heap = []
        for unc in self.twin[userId]:
            for tweets in self.tweet[unc]:
                heapq.heappush(heap, tweets)
        while len(news) < 10 and heap:
            gen, ID = heapq.heappop(heap)
            news.append(ID)
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.tweet:
            self.tweet[followerId] = deque()

        if followerId not in self.twin:
            self.twin[followerId] = set()
            self.twin[followerId].add(followerId)
            
        self.twin[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.twin[followerId]:
            self.twin[followerId].remove(followeeId)
