import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und GannFans
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'GannFans': 1.0
        })
    )
