import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'AverageLogRange': 1.0
        })
    )
