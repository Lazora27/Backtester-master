import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
