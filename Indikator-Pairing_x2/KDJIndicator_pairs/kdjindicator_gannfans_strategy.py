import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und GannFans
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'GannFans': 1.0
        })
    )
