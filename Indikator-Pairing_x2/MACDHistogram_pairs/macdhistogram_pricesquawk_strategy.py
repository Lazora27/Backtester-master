import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PriceSquawk': 1.0
        })
    )
