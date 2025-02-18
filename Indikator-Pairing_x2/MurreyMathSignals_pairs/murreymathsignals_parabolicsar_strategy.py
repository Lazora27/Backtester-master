import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ParabolicSAR': 1.0
        })
    )
