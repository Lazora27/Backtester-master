import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
