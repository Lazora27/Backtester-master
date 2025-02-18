import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'PhaseDivergence': 1.0
        })
    )
