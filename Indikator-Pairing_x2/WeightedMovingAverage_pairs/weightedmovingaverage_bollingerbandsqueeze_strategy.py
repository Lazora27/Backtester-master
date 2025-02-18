import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
