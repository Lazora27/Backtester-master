import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AdaptiveATR': 1.0
        })
    )
