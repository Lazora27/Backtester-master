import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'TimeCycle': 1.0
        })
    )
