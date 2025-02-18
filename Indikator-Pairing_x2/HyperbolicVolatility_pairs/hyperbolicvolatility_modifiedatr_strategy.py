import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'ModifiedATR': 1.0
        })
    )
