import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'PhaseDivergence': 1.0
        })
    )
