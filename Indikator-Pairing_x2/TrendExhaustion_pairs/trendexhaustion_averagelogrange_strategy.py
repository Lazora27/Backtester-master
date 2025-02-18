import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AverageLogRange': 1.0
        })
    )
