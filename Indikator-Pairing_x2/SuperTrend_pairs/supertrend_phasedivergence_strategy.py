import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'PhaseDivergence': 1.0
        })
    )
