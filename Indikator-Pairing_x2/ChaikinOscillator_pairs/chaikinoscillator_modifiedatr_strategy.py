import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
