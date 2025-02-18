import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
