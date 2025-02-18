import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
