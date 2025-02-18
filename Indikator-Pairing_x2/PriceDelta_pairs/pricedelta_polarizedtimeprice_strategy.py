import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
