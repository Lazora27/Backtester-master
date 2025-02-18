import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
