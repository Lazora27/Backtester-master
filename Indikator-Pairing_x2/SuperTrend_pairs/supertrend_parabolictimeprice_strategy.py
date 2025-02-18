import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
