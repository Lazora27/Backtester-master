import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'LiquidityIndex': 1.0
        })
    )
