class dictionary:

    def __init__(self):
         

        self.chest = {"points" : 10, "arenaVal": 5, "image": 'ASSETS/treasures/chest.png'}
        self.coin = {"points" : 20, "arenaVal": 6, "image": 'ASSETS/treasures/coin.png'}
        self.crown = {"points": 15, "arenaVal": 7, "image": 'ASSETS/treasures/crown.png'}
        self.diamond = {"points" : 9, "arenaVal": 8, "image": 'ASSETS/treasures/diamond.png'}
        self.diamondblock = {"points" : 81, "arenaVal": 9, "image": 'ASSETS/treasures/diamondblock.png'}
        self.emerald = {"points": 11, "arenaVal": 10, "image": 'ASSETS/treasures/emerald.png'}
        self.emeraldblock = {"points": 99, "arenaVal": 11, "image": 'ASSETS/treasures/emeraldblock.png'}
        self.goldbar = {"points": 8, "arenaVal": 12, "image": 'ASSETS/treasures/goldbar.png'}
        self.goldblock = {"points": 64, "arenaVal": 13, "image": 'ASSETS/treasures/goldblock.png'}
        self.iron = {"points": 7, "arenaVal": 14, "image": 'ASSETS/treasures/iron.png'}
        self.lapis = {"points": 4, "arenaVal": 15, "image": 'ASSETS/treasures/lapis.png'}
        self.lapisblock = {"points": 36, "arenaVal": 16, "image": 'ASSETS/treasures/lapisblock.png'}
        self.ring = {"points": 30, "arenaVal": 17, "image": 'ASSETS/treasures/ring.png'}
        self.sword = {"points": 40, "arenaVal": 18, "image": 'ASSETS/treasures/sword.png'}
        self.tiara = {"points" : 100, "arenaVal": 19, "image": 'ASSETS/treasures/tiara.png'}
        self.itemList = dict(chest=self.chest, coins=self.coin, crown=self.crown, diamond=self.diamond, diamondblock=self.diamondblock, emerald=self.emerald,emeraldblock=self.emeraldblock, goldbar=self.goldbar, goldblock=self.goldblock, iron=self.iron,lapis=self.lapis, lapisblock=self.lapisblock, ring=self.ring, sword=self.sword,tiara=self.tiara)
