import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'ProjectionBands': 1.0
        })
    )
