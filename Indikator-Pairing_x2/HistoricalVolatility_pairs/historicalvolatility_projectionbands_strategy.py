import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'ProjectionBands': 1.0
        })
    )
