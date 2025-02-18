import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ModifiedATR': 1.0
        })
    )
