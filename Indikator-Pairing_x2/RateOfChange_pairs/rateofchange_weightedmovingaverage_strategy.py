import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
