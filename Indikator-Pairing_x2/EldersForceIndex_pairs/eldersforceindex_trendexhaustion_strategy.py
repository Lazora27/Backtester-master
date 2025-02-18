import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
