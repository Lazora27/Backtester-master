import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und MassIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'MassIndex': 1.0
        })
    )
