import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CenterOfGravity': 1.0
        })
    )
