import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
