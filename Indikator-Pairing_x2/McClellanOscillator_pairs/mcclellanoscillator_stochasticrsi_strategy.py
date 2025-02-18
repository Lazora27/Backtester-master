import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
