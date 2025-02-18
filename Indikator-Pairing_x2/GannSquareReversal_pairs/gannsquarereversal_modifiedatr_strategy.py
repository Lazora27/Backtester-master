import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ModifiedATR': 1.0
        })
    )
