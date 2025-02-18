import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
