import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
