import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
