import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
