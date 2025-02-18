import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PhaseDivergence': 1.0
        })
    )
