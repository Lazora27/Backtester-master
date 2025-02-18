import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PhaseDivergence': 1.0
        })
    )
