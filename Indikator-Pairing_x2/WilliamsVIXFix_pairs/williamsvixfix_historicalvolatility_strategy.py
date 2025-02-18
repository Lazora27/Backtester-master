import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
