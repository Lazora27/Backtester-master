import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ModifiedATR': 1.0
        })
    )
