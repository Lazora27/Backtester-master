import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
