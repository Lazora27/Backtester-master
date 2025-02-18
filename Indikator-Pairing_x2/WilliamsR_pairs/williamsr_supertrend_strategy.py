import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SuperTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SuperTrend': 1.0
        })
    )
