import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DonchianChannels': 1.0
        })
    )
