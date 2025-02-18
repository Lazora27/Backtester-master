import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'PhaseDivergence': 1.0
        })
    )
