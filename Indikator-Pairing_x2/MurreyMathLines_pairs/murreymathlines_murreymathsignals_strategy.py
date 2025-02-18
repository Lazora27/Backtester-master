import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
