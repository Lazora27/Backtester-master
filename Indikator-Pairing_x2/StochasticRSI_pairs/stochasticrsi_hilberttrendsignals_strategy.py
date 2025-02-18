import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
