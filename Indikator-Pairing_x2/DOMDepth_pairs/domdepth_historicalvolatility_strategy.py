import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
