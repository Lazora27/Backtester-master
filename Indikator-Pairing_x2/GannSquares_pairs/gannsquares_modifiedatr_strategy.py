import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ModifiedATR': 1.0
        })
    )
