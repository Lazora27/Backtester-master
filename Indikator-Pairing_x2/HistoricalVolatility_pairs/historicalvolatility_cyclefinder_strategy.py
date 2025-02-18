import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'CycleFinder': 1.0
        })
    )
