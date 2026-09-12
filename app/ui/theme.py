import wx

from app.config import BLUE, BLUE_DARK, BORDER, TEXT, WHITE

def colour(rgb):
  return wx.Colour(*rgb)

def apply_font(control, size=10, bold=False):
  weight = wx.FONTWEIGHT_BOLD if bold else wx.FONTWEIGHT_NORMAL
  control.SetFont(wx.font(size, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, weight))

def accessible(control, name, help_text=""):
  try:
    control.SetName(name)
  except Exception:
    pass
  if help_text:
    try:
      control.SetHelpText(help_text)
    except Exception:
      pass

def button_style(button, primary=False, danger=False):
  apply_font(button, 10, True)
  button.SetMinSize((-1, 40))
  if primary:
    button.SetBackgroundColour(colour(BLUE))
    button.SetForegroundColour(colour(WHITE))
    _bind_hover(button, colour(BLUE), colour(BLUE_DARK))
  elif danger:
    button.SetBackgroundColour(colour((176, 39, 39)))
    button.SetForegroundColour(colour(WHITE))
    _bind_hover(button, colour((176, 39, 39)), colour((140, 28, 28)))
  else:
    button.SetBackgroundColour(colour(WHITE))
    button.SetForegroundColour(colour(TEXT))
    _bind_hover(button, colour(WHITE), colour((235, 240, 245)))

def _bind_hover(button, normal, hover):
  def on_enter(event):
    button.SetBackgroundColour(hover)
    button.Refresh()
    event.Skip()

  def on_leave(event):
    button.SetBackgroundColour(normal)
    button.Refresh()
    event.Skip()

  button.Bind(wx.EVT_ENTER_WINDOW, on_enter)
  button.Bind(wx.EVT_LEAVE_WINDOW, on_leave)

def add_focus_border(control):
