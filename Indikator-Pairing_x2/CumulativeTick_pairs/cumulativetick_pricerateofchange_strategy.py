import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
