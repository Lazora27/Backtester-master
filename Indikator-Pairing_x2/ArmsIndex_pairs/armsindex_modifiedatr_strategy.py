import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
