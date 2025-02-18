import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TrendExhaustion': 1.0
        })
    )
