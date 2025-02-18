import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
