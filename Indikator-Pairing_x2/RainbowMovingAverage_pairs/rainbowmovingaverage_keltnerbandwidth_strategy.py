import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
