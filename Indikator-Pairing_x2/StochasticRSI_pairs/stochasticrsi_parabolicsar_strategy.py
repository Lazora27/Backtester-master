import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
