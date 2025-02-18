import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
