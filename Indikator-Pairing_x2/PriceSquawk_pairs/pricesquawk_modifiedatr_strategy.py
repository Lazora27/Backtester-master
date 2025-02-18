import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ModifiedATR': 1.0
        })
    )
