import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'StochasticRSI': 1.0
        })
    )
