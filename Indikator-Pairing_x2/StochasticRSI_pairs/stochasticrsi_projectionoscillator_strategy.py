import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
