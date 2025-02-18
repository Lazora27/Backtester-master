import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
