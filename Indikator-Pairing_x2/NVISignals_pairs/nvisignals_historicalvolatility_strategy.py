import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
