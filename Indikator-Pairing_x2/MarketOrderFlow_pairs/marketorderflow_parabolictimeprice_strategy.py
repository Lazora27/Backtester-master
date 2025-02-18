import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
