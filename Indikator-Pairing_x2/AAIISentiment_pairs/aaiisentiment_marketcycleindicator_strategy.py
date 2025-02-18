import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
