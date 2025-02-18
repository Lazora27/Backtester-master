import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DonchianChannels': 1.0
        })
    )
