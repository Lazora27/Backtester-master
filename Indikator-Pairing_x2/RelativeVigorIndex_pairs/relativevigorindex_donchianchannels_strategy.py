import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
