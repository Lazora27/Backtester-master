import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
