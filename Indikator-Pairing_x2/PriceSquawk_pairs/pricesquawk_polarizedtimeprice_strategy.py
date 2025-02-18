import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
