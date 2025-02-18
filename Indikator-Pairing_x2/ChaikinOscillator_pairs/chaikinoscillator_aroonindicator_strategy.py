import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AroonIndicator': 1.0
        })
    )
