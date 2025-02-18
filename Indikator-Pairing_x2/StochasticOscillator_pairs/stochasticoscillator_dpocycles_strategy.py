import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
