import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MovingAverage': 1.0
        })
    )
