import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
