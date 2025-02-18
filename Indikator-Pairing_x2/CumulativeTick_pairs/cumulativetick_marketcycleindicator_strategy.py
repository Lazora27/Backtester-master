import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
