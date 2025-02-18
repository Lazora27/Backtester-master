import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
