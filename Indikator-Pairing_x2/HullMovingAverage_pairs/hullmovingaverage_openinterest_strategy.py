import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'OpenInterest': 1.0
        })
    )
