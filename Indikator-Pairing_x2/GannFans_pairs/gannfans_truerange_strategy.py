import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TrueRange
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TrueRange': 1.0
        })
    )
