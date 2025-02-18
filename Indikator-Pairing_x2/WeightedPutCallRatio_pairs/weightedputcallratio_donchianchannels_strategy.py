import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'DonchianChannels': 1.0
        })
    )
