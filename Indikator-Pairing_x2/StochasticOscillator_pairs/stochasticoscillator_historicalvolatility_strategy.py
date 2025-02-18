import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
