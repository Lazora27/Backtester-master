import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TrendCycles': 1.0
        })
    )
