import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
