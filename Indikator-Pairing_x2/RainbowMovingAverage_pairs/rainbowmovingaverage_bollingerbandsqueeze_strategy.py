import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
