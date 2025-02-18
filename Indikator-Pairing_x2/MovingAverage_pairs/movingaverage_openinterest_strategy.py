import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'OpenInterest': 1.0
        })
    )
