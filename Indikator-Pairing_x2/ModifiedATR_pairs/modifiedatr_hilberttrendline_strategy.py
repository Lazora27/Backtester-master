import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'HilbertTrendline': 1.0
        })
    )
