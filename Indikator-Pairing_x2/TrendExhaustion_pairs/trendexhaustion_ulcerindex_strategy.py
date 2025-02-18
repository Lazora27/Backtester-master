import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'UlcerIndex': 1.0
        })
    )
