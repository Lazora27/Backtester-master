import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
