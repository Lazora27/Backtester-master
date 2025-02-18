import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
