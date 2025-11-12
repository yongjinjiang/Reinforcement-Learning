import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Multi-Armed Bandit Demo
# Bernoulli arms; compare Epsilon-Greedy, UCB1, Thompson Sampling
# -----------------------------

class BernoulliBanditEnv:
    def __init__(self, probs, seed=0):
        self.probs = np.array(probs, dtype=float)
        self.rng = np.random.default_rng(seed)
        self.opt_idx = int(np.argmax(self.probs))
        self.opt_mean = float(np.max(self.probs))

    def step(self, action):
        # 0/1 reward from Bernoulli(p_action)
        p = self.probs[action]
        return self.rng.random() < p

    def best(self):
        return self.opt_idx, self.opt_mean


class EpsilonGreedy:
    def __init__(self, n_arms, epsilon=0.1, decay=None, seed=0):
        self.n = n_arms
        self.epsilon = float(epsilon)
        self.decay = decay  # e.g., lambda t, eps: max(0.01, eps*0.999)
        self.counts = np.zeros(self.n, dtype=int)
        self.values = np.zeros(self.n, dtype=float)
        self.rng = np.random.default_rng(seed)

    def select_action(self, t):
        eps = self.epsilon if self.decay is None else self.decay(t, self.epsilon)
        if self.rng.random() < eps:
            return self.rng.integers(self.n)
        else:
            return int(np.argmax(self.values))

    def update(self, a, r):
        self.counts[a] += 1
        n = self.counts[a]
        self.values[a] += (r - self.values[a]) / n


class UCB1:
    def __init__(self, n_arms):
        self.n = n_arms
        self.counts = np.zeros(self.n, dtype=int)
        self.values = np.zeros(self.n, dtype=float)
        self.t = 0

    def select_action(self, t):
        self.t += 1
        # ensure each arm pulled once
        for a in range(self.n):
            if self.counts[a] == 0:
                return a
        bonus = np.sqrt((2.0 * np.log(self.t)) / self.counts)
        return int(np.argmax(self.values + bonus))

    def update(self, a, r):
        self.counts[a] += 1
        n = self.counts[a]
        self.values[a] += (r - self.values[a]) / n


class ThompsonSamplingBernoulli:
    def __init__(self, n_arms, alpha0=1.0, beta0=1.0, seed=0):
        self.n = n_arms
        self.alpha = np.ones(self.n)*alpha0
        self.beta = np.ones(self.n)*beta0
        self.rng = np.random.default_rng(seed)

    def select_action(self, t):
        samples = self.rng.beta(self.alpha, self.beta)
        return int(np.argmax(samples))

    def update(self, a, r):
        self.alpha[a] += r
        self.beta[a]  += (1-r)


def run_sim(env, agent, T):
    K = len(env.probs)
    opt_idx, opt_mean = env.best()
    rewards = np.zeros(T, dtype=float)
    regret = np.zeros(T, dtype=float)
    pulls = np.zeros(K, dtype=int)
    for t in range(1, T+1):
        a = agent.select_action(t)
        r = float(env.step(a))
        agent.update(a, r)
        rewards[t-1] = r
        pulls[a] += 1
        regret[t-1] = opt_mean - env.probs[a]
    return np.cumsum(rewards), np.cumsum(regret), pulls


def main():
    rng = np.random.default_rng(42)
    K = 10
    # Random but diverse arm difficulties
    probs = np.sort(rng.beta(2, 5, size=K))[::-1]
    # Shuffle arms so the agent doesn't know which is best
    probs = probs[rng.permutation(K)]
    print("True Bernoulli means for", K, "arms:")
    print(np.round(probs, 3))

    env = BernoulliBanditEnv(probs, seed=123)
    T = 10000

    # Define agents
    eps_decay = lambda t, eps: max(0.01, eps * 0.9995)
    agents = {
        "EpsilonGreedy(ε-decay)": EpsilonGreedy(K, epsilon=0.2, decay=eps_decay, seed=0),
        "UCB1": UCB1(K),
        "ThompsonSampling": ThompsonSamplingBernoulli(K, seed=1),
    }

    results = {}
    for name, agent in agents.items():
        env = BernoulliBanditEnv(probs, seed=123)
        cum_reward, cum_regret, pulls = run_sim(env, agent, T)
        results[name] = (cum_reward, cum_regret, pulls)

    # Plot cumulative regret
    plt.figure(figsize=(8, 5))
    for name, (_, cum_regret, _) in results.items():
        plt.plot(np.arange(1, T+1), cum_regret, label=name)
    plt.xlabel("Time steps"); plt.ylabel("Cumulative regret")
    plt.title("Multi-Armed Bandit: Cumulative Regret")
    plt.legend(); plt.tight_layout(); plt.savefig("mab_regret.png", dpi=160)
    print("Saved plot to mab_regret.png")

    # Print how many times each algorithm pulled the optimal arm
    opt_idx = int(np.argmax(probs))
    for name, (_, _, pulls) in results.items():
        print(f"{name:>22s} optimal arm pulls: {pulls[opt_idx]} / {T}")

if __name__ == "__main__":
    main()
