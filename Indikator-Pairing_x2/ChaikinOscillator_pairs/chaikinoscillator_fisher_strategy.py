import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und Fisher
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'Fisher': 1.0
        })
    )
