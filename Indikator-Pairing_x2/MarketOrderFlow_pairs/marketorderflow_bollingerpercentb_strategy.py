import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'BollingerPercentB': 1.0
        })
    )
