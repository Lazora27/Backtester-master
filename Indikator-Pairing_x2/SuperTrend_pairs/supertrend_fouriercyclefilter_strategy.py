import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
