import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MovingAverage
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MovingAverage': 1.0
        })
    )
