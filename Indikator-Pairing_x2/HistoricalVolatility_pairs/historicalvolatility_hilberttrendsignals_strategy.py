import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
