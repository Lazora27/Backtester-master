import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
