import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
