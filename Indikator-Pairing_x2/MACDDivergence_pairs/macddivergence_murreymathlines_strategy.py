import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MurreyMathLines': 1.0
        })
    )
