import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'CyberCycle': 1.0
        })
    )
