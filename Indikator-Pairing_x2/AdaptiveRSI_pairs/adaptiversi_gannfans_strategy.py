import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'GannFans': 1.0
        })
    )
