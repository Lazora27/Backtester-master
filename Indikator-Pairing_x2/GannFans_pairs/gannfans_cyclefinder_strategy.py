import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und CycleFinder
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'CycleFinder': 1.0
        })
    )
