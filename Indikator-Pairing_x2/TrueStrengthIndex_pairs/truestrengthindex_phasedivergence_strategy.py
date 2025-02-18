import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
