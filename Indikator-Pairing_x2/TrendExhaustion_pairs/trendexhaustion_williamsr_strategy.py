import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'WilliamsR': 1.0
        })
    )
