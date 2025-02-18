import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
