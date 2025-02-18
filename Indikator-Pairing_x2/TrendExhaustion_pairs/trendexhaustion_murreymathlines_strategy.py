import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'MurreyMathLines': 1.0
        })
    )
