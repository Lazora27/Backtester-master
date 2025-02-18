import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PriceSquawk': 1.0
        })
    )
