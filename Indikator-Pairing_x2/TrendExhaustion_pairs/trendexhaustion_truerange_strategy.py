import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TrueRange
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TrueRange': 1.0
        })
    )
