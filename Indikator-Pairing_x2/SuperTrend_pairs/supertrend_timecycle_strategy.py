import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TimeCycle': 1.0
        })
    )
