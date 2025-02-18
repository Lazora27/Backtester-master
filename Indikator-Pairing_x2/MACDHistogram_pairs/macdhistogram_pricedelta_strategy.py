import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PriceDelta
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PriceDelta': 1.0
        })
    )
