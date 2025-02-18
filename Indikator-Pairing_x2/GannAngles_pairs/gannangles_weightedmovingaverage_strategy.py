import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
