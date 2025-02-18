import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
