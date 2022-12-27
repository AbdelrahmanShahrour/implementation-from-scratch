import numpy as np

class AdamOptimizer:
  def __init__(self, learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8):
    self.learning_rate = learning_rate
    self.beta_1 = beta_1
    self.beta_2 = beta_2
    self.epsilon = epsilon
    self.m_t = None
    self.v_t = None
    self.t = 0

  def update(self, params, grads):
    if self.m_t is None:
      self.m_t = []
      self.v_t = []
      for param in params:
        self.m_t.append(np.zeros_like(param))
        self.v_t.append(np.zeros_like(param))

    self.t += 1
    alpha_t = self.learning_rate * np.sqrt(1 - self.beta_2**self.t) / (1 - self.beta_1**self.t)
    for i, (param, grad) in enumerate(zip(params, grads)):
      self.m_t[i] = self.beta_1 * self.m_t[i] + (1 - self.beta_1) * grad
      self.v_t[i] = self.beta_2 * self.v_t[i] + (1 - self.beta_2) * grad**2
      param -= alpha_t * self.m_t[i] / (np.sqrt(self.v_t[i]) + self.epsilon)