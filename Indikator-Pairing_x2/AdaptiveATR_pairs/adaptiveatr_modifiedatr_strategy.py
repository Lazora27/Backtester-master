import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'ModifiedATR': 1.0
        })
    )
