import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
