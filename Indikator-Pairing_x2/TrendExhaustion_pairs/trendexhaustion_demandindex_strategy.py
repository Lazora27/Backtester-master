import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DemandIndex': 1.0
        })
    )
