import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
