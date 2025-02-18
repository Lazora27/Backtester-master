import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'AccelerationBands': 1.0
        })
    )
