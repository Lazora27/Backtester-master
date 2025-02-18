import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'FearGreedIndex': 1.0
        })
    )
