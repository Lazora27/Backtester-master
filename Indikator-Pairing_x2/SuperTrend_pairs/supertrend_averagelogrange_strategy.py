import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'AverageLogRange': 1.0
        })
    )
