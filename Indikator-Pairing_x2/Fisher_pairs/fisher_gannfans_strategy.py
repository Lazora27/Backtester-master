import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und GannFans
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'GannFans': 1.0
        })
    )
