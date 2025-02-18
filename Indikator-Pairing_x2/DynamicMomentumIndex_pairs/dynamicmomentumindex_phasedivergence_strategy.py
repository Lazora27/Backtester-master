import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
