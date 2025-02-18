import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
