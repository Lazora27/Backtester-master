import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'VolumeDelta': 1.0
        })
    )
