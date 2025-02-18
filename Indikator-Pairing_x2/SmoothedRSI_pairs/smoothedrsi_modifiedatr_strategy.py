import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
