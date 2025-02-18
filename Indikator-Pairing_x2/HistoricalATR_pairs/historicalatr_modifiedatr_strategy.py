import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'ModifiedATR': 1.0
        })
    )
