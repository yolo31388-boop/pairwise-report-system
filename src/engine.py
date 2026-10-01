"""举报处罚 - 带8个bug"""
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Report:
    rid: str
    reporter: str
    reported: str
    content: str
    context: list
    status: str

class ReportSystem:
    def __init__(self):
        self.reports: list[Report] = []
        self.penalties = {}
        self.banned = set()

    def submit(self, reporter, reported, content):
        # bug1: 不检查举报人状态
        r = Report(f"r{len(self.reports)}", reporter, reported, content, [], "pending")
        self.reports.append(r)
        return r

    def auto_filter(self, content):
        # bug2: 无自动过滤
        return False

    def merge_duplicates(self):
        # bug3: 不合并
        pass

    def penalize(self, reported, violation_count):
        # bug4: 固定处罚
        return {"type": "mute", "duration": 3600}

    def get_evidence(self, rid):
        # bug5: 只存截图
        return {"screenshot": "img.png"}

    def notify_reporter(self, rid):
        # bug6: 不通知
        pass

    def can_appeal(self, penalty_id, penalty_time):
        # bug7: 无时间限制
        return True

    def compensate_false_ban(self, player_id, duration):
        # bug8: 不补偿
        return {}
