import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
