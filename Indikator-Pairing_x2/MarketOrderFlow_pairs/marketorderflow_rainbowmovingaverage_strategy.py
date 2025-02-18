import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
