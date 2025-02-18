import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
