import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
