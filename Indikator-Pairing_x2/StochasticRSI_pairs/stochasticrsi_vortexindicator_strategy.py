import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VortexIndicator': 1.0
        })
    )
