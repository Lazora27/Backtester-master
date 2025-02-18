import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
