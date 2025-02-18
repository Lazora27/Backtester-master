import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'BradleySiderograph': 1.0
        })
    )
