import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'AccelerationBands': 1.0
        })
    )
