import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
