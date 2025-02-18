import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BuyingPressure': 1.0
        })
    )
