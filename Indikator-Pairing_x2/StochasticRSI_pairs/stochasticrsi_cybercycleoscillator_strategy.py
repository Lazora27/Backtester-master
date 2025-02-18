import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
