import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
