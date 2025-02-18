import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'StochasticRSI': 1.0
        })
    )
