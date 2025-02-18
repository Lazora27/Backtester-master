import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
