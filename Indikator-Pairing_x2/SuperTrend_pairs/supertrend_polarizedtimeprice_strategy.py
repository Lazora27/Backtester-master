import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
