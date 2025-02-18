import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
