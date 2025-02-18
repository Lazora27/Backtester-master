import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
