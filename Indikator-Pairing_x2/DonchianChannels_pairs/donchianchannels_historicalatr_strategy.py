import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HistoricalATR': 1.0
        })
    )
