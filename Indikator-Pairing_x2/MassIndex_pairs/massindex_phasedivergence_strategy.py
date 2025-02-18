import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
