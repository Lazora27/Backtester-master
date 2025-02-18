import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und MassIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'MassIndex': 1.0
        })
    )
