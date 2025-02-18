import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'UlcerIndex': 1.0
        })
    )
