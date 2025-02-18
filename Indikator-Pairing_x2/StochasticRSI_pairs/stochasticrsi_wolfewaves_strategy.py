import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
