import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MACDHistogram': 1.0
        })
    )
