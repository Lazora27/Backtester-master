import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ModifiedATR': 1.0
        })
    )
