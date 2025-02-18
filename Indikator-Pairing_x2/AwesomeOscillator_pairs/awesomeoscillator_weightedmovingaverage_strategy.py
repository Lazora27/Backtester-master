import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
