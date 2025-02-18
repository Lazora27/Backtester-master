import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
