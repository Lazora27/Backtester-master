import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DonchianChannels': 1.0
        })
    )
