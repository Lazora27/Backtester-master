import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'KeltnerChannels': 1.0
        })
    )
