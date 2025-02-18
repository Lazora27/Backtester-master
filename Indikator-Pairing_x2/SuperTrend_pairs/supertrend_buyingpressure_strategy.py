import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BuyingPressure': 1.0
        })
    )
