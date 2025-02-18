import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
