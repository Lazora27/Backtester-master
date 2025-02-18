import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
