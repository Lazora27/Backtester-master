import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'AverageTrueRange': 1.0
        })
    )
