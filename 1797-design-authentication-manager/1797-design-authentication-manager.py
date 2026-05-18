class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.expire = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expire[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        exp_time = self.expire.get(tokenId)
        if exp_time is None or exp_time <= currentTime:
            return
        self.expire[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(exp > currentTime for exp in self.expire.values())