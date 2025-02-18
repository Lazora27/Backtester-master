import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
