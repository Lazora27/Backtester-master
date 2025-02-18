import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
