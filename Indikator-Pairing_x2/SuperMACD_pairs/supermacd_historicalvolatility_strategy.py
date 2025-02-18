import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
