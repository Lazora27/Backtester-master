import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
