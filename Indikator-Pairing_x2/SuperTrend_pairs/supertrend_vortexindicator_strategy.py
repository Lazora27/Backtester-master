import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'VortexIndicator': 1.0
        })
    )
