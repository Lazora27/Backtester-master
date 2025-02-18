import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
