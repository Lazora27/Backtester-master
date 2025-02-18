import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
