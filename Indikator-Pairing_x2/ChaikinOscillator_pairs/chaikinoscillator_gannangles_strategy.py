import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
