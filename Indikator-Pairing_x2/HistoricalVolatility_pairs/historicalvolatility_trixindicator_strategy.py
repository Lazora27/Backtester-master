import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'TRIXIndicator': 1.0
        })
    )
