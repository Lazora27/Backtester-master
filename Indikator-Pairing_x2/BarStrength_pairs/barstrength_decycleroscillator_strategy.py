import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
