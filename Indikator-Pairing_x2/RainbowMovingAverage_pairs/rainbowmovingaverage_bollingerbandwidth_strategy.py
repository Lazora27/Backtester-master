import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
