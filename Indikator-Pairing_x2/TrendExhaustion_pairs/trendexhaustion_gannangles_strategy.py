import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und GannAngles
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'GannAngles': 1.0
        })
    )
