import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TrendExhaustion': 1.0
        })
    )
