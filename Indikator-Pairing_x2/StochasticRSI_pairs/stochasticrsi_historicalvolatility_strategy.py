import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
