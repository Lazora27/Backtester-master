import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'ModifiedATR': 1.0
        })
    )
