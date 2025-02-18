import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DonchianChannels': 1.0
        })
    )
