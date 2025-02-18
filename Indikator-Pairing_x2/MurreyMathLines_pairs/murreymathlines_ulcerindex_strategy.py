import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'UlcerIndex': 1.0
        })
    )
