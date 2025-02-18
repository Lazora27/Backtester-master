import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DonchianChannels': 1.0
        })
    )
