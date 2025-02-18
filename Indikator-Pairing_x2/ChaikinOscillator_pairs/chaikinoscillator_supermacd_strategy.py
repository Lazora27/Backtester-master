import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
