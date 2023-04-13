"""
20230413
실버3 파일 정리
url: https://www.acmicpc.net/problem/20291
후기: 단순 문자열 파싱이다.
파일 이름에 '.'이 반드시 하나밖에 없어서 더욱 쉬웠다.
마지막에 sorted의 기준을 넣지 않았는데, 기본적으로 알파벳을 사전순으로 정렬해주고, count를 기준으로 정렬이 되든 안되든 상관이 없기 때문이다.
"""

from sys import stdin

class Dictionary(dict):
    def count(self, key):
        if key in self.keys():
            self[key] += 1
        else:
            self[key] = 1

def countExtension():
    extension_count = Dictionary()

    file_count = int(stdin.readline().strip())
    for _ in range(file_count):
        file = stdin.readline().strip()
        name, extension = file.split('.')
        extension_count.count(extension)

    return extension_count

extension_count = countExtension()
extension_count = list(extension_count.items())
for extension, count in sorted(extension_count):
    print(extension, count)
