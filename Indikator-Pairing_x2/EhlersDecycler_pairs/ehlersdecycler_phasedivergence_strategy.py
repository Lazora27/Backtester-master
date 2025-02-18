import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'PhaseDivergence': 1.0
        })
    )
