import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CenterOfGravity': 1.0
        })
    )
