import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ModifiedATR': 1.0
        })
    )
