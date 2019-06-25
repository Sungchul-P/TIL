# LeagueTable 클래스는 리그의 각 플레이어 점수를 추적합니다. 
# 각 게임 후에 플레이어는 record_result 함수로 점수를 기록합니다.

# 리그에서 플레이어의 순위는 다음 논리를 사용하여 계산됩니다.

# 1. 점수가 가장 높은 플레이어가 1 위 입니다. 점수가 가장 낮은 플레이어는 마지막으로 순위가 매겨집니다.
# 2. 두 명의 플레이어의 점수가 동일하다면, 게임 플레이 횟수가 적은 플레이어가 더 높은 순위로 기록됩니다.
# 3. 두 명의 플레이어가 점수와 게임 플레이 횟수 모두 동일하면, 선수명단의 앞쪽에 위치한 선수가 더 높게 기록됩니다.

# 주어진 순위의 플레이어를 반환하는 player_rank 함수를 구현하십시오.

# 문제 원형 #
'''
from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        return None
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))
'''

# 문제 풀이 #
from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        # self.standings[player] => Counter()
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        srt = sorted(
                self.standings.items(),
                key=lambda kv: (
                    -kv[1]['score'], # 내림차순 정렬
                    kv[1]['games_played'], # 오름차순 정렬
                ),
                reverse=False)
        # print(srt)
        # [('Chris', Counter({'score': 5, 'games_played': 1})), 
        # ('Arnold', Counter({'score': 5, 'games_played': 1})), 
        # ('Mike', Counter({'score': 5, 'games_played': 2}))]
        return srt[rank - 1][0]
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))