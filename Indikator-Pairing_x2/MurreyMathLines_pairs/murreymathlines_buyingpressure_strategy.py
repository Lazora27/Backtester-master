import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'BuyingPressure': 1.0
        })
    )
