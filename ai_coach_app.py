# ai_coach_app.py
import statistics
from collections import Counter

def classify_odd_even(num):
    return "Odd" if num % 2 != 0 else "Even"

def count_distribution():
    odds = len([x for x in range(3, 19) if classify_odd_even(x) == "Odd"])
    evens = len([x for x in range(3, 19) if classify_odd_even(x) == "Even"])
    return odds, evens

class AICoach:
    def __init__(self):
        self.memory = []
        self.stake_plan = [10, 20, 35, 60, 90, 140, 210, 300]
        self.total_profit = 0
        self.balance = 1000
        self.current_round = 0
        self.win_log = []
        self.loss_log = []
        self.last_prediction = None
        self.last_predicted_number = None

    def learn(self, result):
        self.memory.append(result)
        if len(self.memory) > 100:
            self.memory.pop(0)

    def get_streak_info(self):
        if len(self.memory) < 4:
            return "Stable"
        last = [classify_odd_even(x) for x in self.memory[-4:]]
        if all(x == last[0] for x in last):
            return "Strong Repetition"
        elif last[-1] != last[-2] != last[-3]:
            return "Flip Potential"
        return "Mixed"

    def quantum_guess_range(self):
        if not self.memory:
            return [10, 11, 12]
        avg = round(statistics.mean(self.memory[-10:]))
        return [avg-1, avg, avg+1]

    def predict_next(self):
        data = self.memory[-30:]
        if len(data) < 10:
            return "Even", 50, 10, "Not enough data yet"

        trends = [classify_odd_even(x) for x in data]
        odd_count = trends.count("Odd")
        even_count = trends.count("Even")

        prediction = "Odd" if odd_count > even_count else "Even"
        confidence = 55 + abs(odd_count - even_count) * 2

        reverse_applied = False
        if len(data) >= 3 and all(classify_odd_even(x) == trends[-1] for x in data[-3:]):
            prediction = "Even" if prediction == "Odd" else "Odd"
            confidence -= 5
            reverse_applied = True

        parity_filtered = [x for x in data if classify_odd_even(x) == prediction]
        hot_number = Counter(parity_filtered).most_common(1)[0][0] if parity_filtered else 10
        self.last_predicted_number = hot_number

        reason = (
            f"Trend: {prediction} | Hot: {hot_number} | Reverse logic: {'Yes' if reverse_applied else 'No'}\n"
            f"Streak: {self.get_streak_info()} | Memory size: {len(self.memory)}"
        )

        self.last_prediction = prediction
        return prediction, min(confidence, 95), hot_number, reason

    def evaluate_result(self, actual_result):
        actual_parity = classify_odd_even(actual_result)
        prediction = self.last_prediction or self.predict_next()[0]
        stake = self.stake_plan[min(self.current_round, len(self.stake_plan) - 1)]

        win = prediction.lower() == actual_parity.lower()

        if win:
            self.balance += stake
            self.total_profit += stake
            self.win_log.append(actual_result)
            self.current_round = 0
        else:
            self.balance -= stake
            self.total_profit -= stake
            self.loss_log.append(actual_result)
            self.current_round += 1

        self.learn(actual_result)
        return win, stake, self.current_round

    def get_summary(self):
        total_predictions = len(self.win_log) + len(self.loss_log)
        accuracy = round((len(self.win_log) / total_predictions) * 100, 2) if total_predictions else 0
        return {
            "wins": len(self.win_log),
            "losses": len(self.loss_log),
            "profit": self.total_profit,
            "balance": self.balance,
            "accuracy": accuracy
        }
