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
    acessible(title, "Título do aplicativo LPSGH Finanças", "Título Principal")

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
    accessible
