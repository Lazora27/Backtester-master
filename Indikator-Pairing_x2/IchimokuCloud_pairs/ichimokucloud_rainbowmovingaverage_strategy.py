import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
