import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
