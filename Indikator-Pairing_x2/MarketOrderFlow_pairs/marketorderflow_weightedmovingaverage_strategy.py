import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
