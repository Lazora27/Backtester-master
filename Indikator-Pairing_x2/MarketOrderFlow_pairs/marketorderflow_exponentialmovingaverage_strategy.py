import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
