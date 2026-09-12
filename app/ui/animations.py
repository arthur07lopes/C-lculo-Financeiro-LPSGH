import wx

def fade_in_window(window, duration_ms=280, steps=14):
  try:
    supported = window.CanSetTransparent()
  except Exception:
    supported = False

  if not supported:
    return

  delay = max(1, duration_ms // steps)
  state = {"step": 0}

  def tick():
    state = {"step"} += 1
    alpha = int(255 * state["step"] / steps)
    try:
      window.SetTransparent(min(255, alpha))
    except Exception:
      return
    if state["step"] < steps:
      wx.CallLater(delay, tick)

  try:
    window.SetTransparent(0)
  except Exception:
    return
  wx.CallLater(delay, tick)

def animate_gauge(gauge, target_value, duration_ms=260, steps=12):
  target_value = max(0, min(100, int(target_value)))
  start_value = gauge.GetValue()
  if start_value == target_value:
    return

  delay = max(1, duration_ms // steps)
  state = {"step": 0}

  def tick():
    state["step"] += 1
    progress = state["step"] / steps
    value = int(start_value + (target_value - start_value) * progress)
    gauge.SetValue(max(0, min(100, value)))
    if state["step"] < steps:
      wx.CallLater(delay, tick)
    else:
      gauge.SetValue(target_value)

  wx.CallLater(delay, tick)
