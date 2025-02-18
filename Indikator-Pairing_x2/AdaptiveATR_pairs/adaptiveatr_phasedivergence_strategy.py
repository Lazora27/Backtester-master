import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'PhaseDivergence': 1.0
        })
    )
