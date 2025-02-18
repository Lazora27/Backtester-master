import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'IntradayIntensity': 1.0
        })
    )
