import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'BollingerBands': 1.0
        })
    )
