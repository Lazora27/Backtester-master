import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'IchimokuCloud': 1.0
        })
    )
