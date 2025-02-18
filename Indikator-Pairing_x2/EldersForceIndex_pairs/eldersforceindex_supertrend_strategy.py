import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
