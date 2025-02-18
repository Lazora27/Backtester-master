import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HistoricalATR': 1.0
        })
    )
