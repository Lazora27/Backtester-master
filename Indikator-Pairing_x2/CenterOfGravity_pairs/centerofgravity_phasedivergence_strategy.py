import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'PhaseDivergence': 1.0
        })
    )
