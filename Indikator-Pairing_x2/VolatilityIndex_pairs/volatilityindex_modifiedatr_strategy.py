import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
