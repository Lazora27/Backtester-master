import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
