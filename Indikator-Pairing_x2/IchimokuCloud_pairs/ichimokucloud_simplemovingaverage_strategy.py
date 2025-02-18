import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
