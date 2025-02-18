import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'BollingerBands': 1.0
        })
    )
