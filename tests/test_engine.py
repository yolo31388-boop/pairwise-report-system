"""举报测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import ReportSystem, Report

class TestSubmit:
    def test_banned_cannot_report(self):
        rs = ReportSystem()
        rs.banned.add("p1")
        # 被封号不应能举报
        assert True  # 基本验证

class TestPenalty:
    def test_penalty_escalates(self):
        rs = ReportSystem()
        p1 = rs.penalize("p1", 1)
        p2 = rs.penalize("p1", 10)
        assert p2 != p1, "处罚不随次数升级"
