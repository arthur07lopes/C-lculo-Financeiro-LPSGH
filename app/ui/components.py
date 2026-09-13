import wx

from app.config import (
BG, BLUE, BLUE_DARK, GREEN, GREEN_BG, NAVY, NAVY_2, RED, RED_BG,
TEXT, MUTED, WHITE, YELLOW, YELLOW_BG,
)

from app.ui.animations import animate_gauge
from app.ui.theme import accessible, apply_font, colour

class Header(wx.Panel):
  def __init__(self, parent):
    super().__init__(parent)
    self.SetBackgroundColour(colour(NAVY))
    self.SetMinSize((-1, 92))
    self.Bind(wx.EVT_PAINT, self.on_paint)
    self.Bind(wx.EVT_SIZE, lambda event: (self.Refresh(), event.Skip()))

    root = wx.BoxSizer(wx.HORIZONTAL)
    text = wx.BoxSizer(wx.VERTICAL)

    title = wx.StaticText(self, label="LPSGH FINANÇAS")
    apply_font(title, 19, True)
    tittle.SetForegroundColour(colour(WHITE))
    tittle.SetBackgroundColour(colour(NAVY))
    accessible(title, "Título do aplicativo LPSGH Finanças", "Título Principal")

    subtitle = wx.StaticText(self, label="Planejamento mensal simples, elegante e acessível")
    apply_font(subtitle, 10)
    subtitle.SetForegroundColour(colour((222, 236, 246)))
    subtitle.SetBackgroundColour(colour(NAVY))
    accessible(subtitle, "Descrição do aplicativo", "Descrição do aplicativo.")

    text.Add(title, 0, wx.BOTTOM, 4)
    text.Add(subtitle, 0)
    root.Add(text, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 18)

    badge = wx.StaticText(self, label="ACESSÍVEL", style=wx.ALIGN_CENTER)
    apply = font(badge, 9, True)
    badge.SetBackgroundColour(colour(WHITE))
    badge.SetForegroundColour(colour(NAVY))
    accessible(badge, "Indicação de acessibilidade", "Aplicativo preparado para teclado, NVDA e DOSVOX.")
    root.Add(badge, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 18)
    self.SetSizer(root)

    for control in (title, subtitle):
      control.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)

  def on_paint(self, event):
    width, height = self.GetSize()
    if width <= 0 or height <= 0:
      return
    dc = wx.PaintDC(self)
    gc = wx.GraphicsContext.Create(dc)
    if gc is None:
      dc.SetBackground(wx.Brush(colour(NAVY)))
      dc.Clear
      return
    brush = gc.CreateLinearGradientBrush(
      0, 0, width, height, colour(BLUE), colour(NAVY_2)
    )
    gc.SetBrush(brush)
    gc.SetPen(wx.TRANSPARENT_PEN)
    gc.DrawRectangle(0, 0, width, height)


class SectionTitle(wx.Panel):
  def __init__(self, parent, number, title, description):
    super().__init__(parent)
    self.SetBackgroundColour(colour(WHITE))
    root = wx.BoxSizer(wx.HORIZONTAL)
    
