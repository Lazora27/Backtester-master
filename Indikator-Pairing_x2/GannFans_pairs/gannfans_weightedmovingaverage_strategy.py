import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
