import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'HilbertSinewave': 1.0
        })
    )
