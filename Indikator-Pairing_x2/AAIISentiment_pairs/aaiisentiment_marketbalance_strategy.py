import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MarketBalance': 1.0
        })
    )
