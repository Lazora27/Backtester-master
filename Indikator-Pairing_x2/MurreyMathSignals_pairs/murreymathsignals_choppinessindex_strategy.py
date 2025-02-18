import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
