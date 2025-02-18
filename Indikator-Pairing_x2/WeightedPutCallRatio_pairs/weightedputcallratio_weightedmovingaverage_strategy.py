import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
