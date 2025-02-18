import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'PhaseDivergence': 1.0
        })
    )
