import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
