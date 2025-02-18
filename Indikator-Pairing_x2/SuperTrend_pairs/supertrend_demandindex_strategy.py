import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und DemandIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'DemandIndex': 1.0
        })
    )
