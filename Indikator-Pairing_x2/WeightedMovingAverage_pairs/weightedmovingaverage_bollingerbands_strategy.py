import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BollingerBands': 1.0
        })
    )
