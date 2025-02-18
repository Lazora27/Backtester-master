import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MurreyMathLines': 1.0
        })
    )
