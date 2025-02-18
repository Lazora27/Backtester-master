import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'PhaseDivergence': 1.0
        })
    )
