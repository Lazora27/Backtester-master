import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
