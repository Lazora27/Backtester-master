import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'CycleFinder': 1.0
        })
    )
