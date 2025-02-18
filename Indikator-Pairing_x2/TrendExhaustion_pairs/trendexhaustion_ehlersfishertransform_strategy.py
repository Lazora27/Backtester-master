import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
