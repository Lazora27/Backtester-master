import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'RateOfChange': 1.0
        })
    )
