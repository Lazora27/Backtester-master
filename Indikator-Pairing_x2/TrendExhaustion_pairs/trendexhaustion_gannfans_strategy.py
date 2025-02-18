import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und GannFans
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'GannFans': 1.0
        })
    )
