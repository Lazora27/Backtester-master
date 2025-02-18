import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
