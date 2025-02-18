import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AccelerationBands': 1.0
        })
    )
