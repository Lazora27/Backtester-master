import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
