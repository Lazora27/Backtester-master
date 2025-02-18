import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TrendCycles': 1.0
        })
    )
