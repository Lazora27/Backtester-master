import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'ModifiedATR': 1.0
        })
    )
