import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TrendExhaustion': 1.0
        })
    )
