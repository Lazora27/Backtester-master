import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'OpenInterest': 1.0
        })
    )
