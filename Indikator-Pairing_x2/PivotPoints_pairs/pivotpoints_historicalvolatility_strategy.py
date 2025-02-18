import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
