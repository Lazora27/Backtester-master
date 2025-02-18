import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TRIXIndicator': 1.0
        })
    )
