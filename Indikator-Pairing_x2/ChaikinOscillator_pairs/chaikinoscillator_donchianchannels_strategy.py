import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'DonchianChannels': 1.0
        })
    )
