import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TrendExhaustion': 1.0
        })
    )
