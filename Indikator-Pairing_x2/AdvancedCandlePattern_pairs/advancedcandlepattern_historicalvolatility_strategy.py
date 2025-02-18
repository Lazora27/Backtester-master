import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
