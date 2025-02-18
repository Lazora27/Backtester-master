import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HistoricalATR': 1.0
        })
    )
