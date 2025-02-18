import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
