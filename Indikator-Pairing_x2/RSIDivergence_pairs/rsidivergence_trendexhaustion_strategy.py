import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TrendExhaustion': 1.0
        })
    )
