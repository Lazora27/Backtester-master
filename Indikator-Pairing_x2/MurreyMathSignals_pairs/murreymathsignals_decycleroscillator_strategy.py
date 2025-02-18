import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
