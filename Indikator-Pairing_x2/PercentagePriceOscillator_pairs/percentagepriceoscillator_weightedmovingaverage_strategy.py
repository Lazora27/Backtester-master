import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
