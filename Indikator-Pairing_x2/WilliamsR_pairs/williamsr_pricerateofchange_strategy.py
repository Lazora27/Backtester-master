import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
