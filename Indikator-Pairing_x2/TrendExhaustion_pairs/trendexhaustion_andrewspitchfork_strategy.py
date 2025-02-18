import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
