import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
