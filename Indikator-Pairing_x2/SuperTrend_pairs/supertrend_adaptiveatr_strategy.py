import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'AdaptiveATR': 1.0
        })
    )
