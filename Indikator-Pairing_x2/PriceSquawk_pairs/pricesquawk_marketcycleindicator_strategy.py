import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
