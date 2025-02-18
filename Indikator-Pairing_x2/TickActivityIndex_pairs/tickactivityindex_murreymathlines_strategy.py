import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
