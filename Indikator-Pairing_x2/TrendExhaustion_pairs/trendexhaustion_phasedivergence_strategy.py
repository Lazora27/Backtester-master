import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PhaseDivergence': 1.0
        })
    )
