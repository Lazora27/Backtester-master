import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'MovingAverage': 1.0
        })
    )
