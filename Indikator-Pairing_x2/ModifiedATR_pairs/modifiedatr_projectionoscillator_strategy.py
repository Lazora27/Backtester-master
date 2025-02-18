import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
