import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
