import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'PhaseDivergence': 1.0
        })
    )
