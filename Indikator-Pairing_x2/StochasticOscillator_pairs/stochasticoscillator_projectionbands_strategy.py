import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
