import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
