import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
