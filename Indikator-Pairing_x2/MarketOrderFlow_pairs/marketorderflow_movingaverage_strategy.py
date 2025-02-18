import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'MovingAverage': 1.0
        })
    )
