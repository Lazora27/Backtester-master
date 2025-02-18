import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MurreyMathLines': 1.0
        })
    )
