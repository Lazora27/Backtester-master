import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'ModifiedATR': 1.0
        })
    )
