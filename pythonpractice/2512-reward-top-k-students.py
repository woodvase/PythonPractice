import heapq
from typing import List


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        pfSet = set(positive_feedback)
        nfSet = set(negative_feedback)
        pq = []
        for index, id in enumerate(student_id):
            s = 0
            r = report[index]
            for w in r.split(" "):
                if w in pfSet:
                    s += 3
                if w in nfSet:
                    s -= 1
            heapq.heappush(pq, (s, -id))
            if len(pq) > k:
                w, i = heapq.heappop(pq)
                print(w, i)

        tmp = []
        while len(pq):
            tmp.append(-heapq.heappop(pq)[1])

        tmp.reverse()
        return tmp


print(
    Solution().topStudents(
        ["fkeofjpc", "qq", "iio"],
        ["jdh", "khj", "eget", "rjstbhe", "yzyoatfyx", "wlinrrgcm"],
        [
            "rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio",
            "gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx",
            "tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe",
            "jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh",
            "yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq",
            "fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v",
            "wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq",
            "d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe",
        ],
        [
            96537918,
            589204657,
            765963609,
            613766496,
            43871615,
            189209587,
            239084671,
            908938263,
        ],
        3,
    )
)


test = [(0, -908938263), (7, -43871615), ((7, -189209587))]
heapq.heapify(test)
print(heapq.heappop(test))
print(heapq.heappop(test))
print(heapq.heappop(test))
