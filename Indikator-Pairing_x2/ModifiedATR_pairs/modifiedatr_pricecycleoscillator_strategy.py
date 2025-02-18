import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
