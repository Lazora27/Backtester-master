import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
