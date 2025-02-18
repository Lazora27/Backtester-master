import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
