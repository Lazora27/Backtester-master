import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
