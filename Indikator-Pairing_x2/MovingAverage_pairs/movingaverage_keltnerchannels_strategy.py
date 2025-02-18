import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'KeltnerChannels': 1.0
        })
    )
