import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'EhlersDecycler': 1.0
        })
    )
