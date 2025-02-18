import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DonchianChannels': 1.0
        })
    )
