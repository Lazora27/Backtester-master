import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AAIISentiment': 1.0
        })
    )
