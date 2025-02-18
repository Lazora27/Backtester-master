import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
