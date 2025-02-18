import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TimeCycle': 1.0
        })
    )
