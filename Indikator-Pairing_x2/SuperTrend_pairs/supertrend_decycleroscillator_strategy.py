import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
