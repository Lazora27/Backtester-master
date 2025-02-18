import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
