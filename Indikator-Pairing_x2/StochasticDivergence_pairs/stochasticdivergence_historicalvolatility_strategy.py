import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
