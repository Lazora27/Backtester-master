import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'MurreyMathLines': 1.0
        })
    )
