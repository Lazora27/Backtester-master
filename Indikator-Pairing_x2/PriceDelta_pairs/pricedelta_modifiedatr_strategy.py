import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ModifiedATR': 1.0
        })
    )
