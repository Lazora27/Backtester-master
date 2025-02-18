import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
