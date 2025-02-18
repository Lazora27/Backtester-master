import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'PhaseDivergence': 1.0
        })
    )
