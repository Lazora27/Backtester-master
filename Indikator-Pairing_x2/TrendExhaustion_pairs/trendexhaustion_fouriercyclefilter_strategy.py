import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
