import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
