import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PriceSquawk': 1.0
        })
    )
