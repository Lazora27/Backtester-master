import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'CyberCycle': 1.0
        })
    )
