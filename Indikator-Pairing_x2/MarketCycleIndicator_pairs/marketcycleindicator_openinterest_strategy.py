import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
