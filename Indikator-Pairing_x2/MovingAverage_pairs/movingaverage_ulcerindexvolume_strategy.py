import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
