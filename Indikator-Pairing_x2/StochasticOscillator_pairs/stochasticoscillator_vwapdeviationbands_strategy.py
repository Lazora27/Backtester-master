import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
