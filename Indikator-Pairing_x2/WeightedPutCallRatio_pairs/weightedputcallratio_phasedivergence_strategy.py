import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'PhaseDivergence': 1.0
        })
    )
