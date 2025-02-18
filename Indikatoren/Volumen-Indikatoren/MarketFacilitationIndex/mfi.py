import backtrader as bt

class MarketFacilitationIndex(bt.Indicator):
    """
    Market Facilitation Index (MFI, Bill Williams)
    
    Misst die Preisbewegung pro Volumeneinheit. Zeigt an, wie effizient der Markt
    Preisänderungen ermöglicht.
    
    Formel:
    MFI = (High - Low) / Volume
    
    Farbkodierung:
    - Grün: MFI steigt, Volumen steigt (Bullen kontrollieren)
    - Braun: MFI fällt, Volumen fällt (Bären kontrollieren)
    - Blau: MFI steigt, Volumen fällt (Marktteilnehmer uneinig)
    - Pink: MFI fällt, Volumen steigt (Blockade)
    
    Parameter:
    - factor (1000000): Skalierungsfaktor für bessere Lesbarkeit
    """
    
    lines = ('mfi', 'mfi_change', 'volume_change')
    params = (('factor', 1000000),)
    
    plotlines = dict(
        mfi=dict(_name='MFI'),
        mfi_change=dict(_plotskip=True),
        volume_change=dict(_plotskip=True)
    )
    
    def __init__(self):
        # Berechne MFI
        self.lines.mfi = (self.data.high - self.data.low) / self.data.volume * self.p.factor
        
        # Berechne Änderungen für Farbkodierung
        self.lines.mfi_change = self.lines.mfi - self.lines.mfi(-1)
        self.lines.volume_change = self.data.volume - self.data.volume(-1)
    
    def next(self):
        # Farbkodierung könnte hier implementiert werden
        if self.lines.mfi_change[0] > 0:
            if self.lines.volume_change[0] > 0:
                # Grün: Bullen kontrollieren
                pass
            else:
                # Blau: Uneinigkeit
                pass
        else:
            if self.lines.volume_change[0] > 0:
                # Pink: Blockade
                pass
            else:
                # Braun: Bären kontrollieren
                pass
