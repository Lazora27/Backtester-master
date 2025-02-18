import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
