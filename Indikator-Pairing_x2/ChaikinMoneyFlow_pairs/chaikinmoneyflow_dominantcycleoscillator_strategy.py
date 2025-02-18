import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinMoneyFlow_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinMoneyFlow und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ChaikinMoneyFlow': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
