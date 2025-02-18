import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
