import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'PhaseDivergence': 1.0
        })
    )
