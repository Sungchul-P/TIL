# 연결리스트(LinkedList) 문제

# 객체에 첫 번째 노래가 반복되어 두 번째 재생되면 반복 재생목록으로 간주한다.
# 반복 확인이 되기 전에 다음 재생 곡(next)이 None인 곡이 있으면, 1회 재생목록으로 판단한다.

# 문제 원형 #
'''
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        return None
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())
'''

# 문제 풀이 #
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    # 재생목록이 반복될 경우 True, 아니면 False.
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs = set() # 속도 향상을 위해 set 사용
        current_song = self
        while current_song:
            # 같은 곡이 두 번째로 확인되면 반복 플레이리스트로 간주한다.
            if current_song.name in songs:
                return True
            else:
                songs.add(current_song.name)
                # 다음 플레이곡을 current_song으로 지정(없는 경우 None)
                current_song = current_song.next

        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())