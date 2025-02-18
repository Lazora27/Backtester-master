import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'WeeklyCycle': 1.0
        })
    )
