import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
