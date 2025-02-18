import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'StochasticOscillator': 1.0
        })
    )
