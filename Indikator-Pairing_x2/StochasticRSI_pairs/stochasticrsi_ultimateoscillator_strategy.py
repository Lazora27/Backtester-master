import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'UltimateOscillator': 1.0
        })
    )
