import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SuperTrend
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SuperTrend': 1.0
        })
    )
