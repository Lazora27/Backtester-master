import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
