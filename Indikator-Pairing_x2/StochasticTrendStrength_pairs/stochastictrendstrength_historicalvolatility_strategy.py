import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
