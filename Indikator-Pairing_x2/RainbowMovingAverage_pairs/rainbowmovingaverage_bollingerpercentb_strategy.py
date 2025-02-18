import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'BollingerPercentB': 1.0
        })
    )
