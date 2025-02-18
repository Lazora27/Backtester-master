import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'KDJIndicator': 1.0
        })
    )
