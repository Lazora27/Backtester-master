import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und MarketBalance
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'MarketBalance': 1.0
        })
    )
