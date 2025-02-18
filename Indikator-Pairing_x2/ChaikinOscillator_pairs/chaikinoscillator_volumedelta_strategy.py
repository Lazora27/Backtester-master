import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'VolumeDelta': 1.0
        })
    )
