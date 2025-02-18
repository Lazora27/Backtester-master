import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
