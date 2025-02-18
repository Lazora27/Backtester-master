import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'GannFans': 1.0
        })
    )
