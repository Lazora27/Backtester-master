import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
