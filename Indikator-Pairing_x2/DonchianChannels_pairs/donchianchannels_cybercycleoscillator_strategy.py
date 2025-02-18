import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
