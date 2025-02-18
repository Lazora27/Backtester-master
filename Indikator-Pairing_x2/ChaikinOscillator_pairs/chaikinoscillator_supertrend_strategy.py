import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
