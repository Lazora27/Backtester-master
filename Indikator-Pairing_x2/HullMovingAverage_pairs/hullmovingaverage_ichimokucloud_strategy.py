import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'IchimokuCloud': 1.0
        })
    )
