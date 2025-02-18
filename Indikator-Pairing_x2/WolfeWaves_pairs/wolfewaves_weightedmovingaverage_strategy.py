import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
