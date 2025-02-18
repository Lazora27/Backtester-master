import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AroonIndicator': 1.0
        })
    )
