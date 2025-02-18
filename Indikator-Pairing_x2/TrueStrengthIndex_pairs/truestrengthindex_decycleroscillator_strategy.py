import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
