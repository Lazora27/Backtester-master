import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
