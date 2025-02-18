import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ModifiedATR': 1.0
        })
    )
