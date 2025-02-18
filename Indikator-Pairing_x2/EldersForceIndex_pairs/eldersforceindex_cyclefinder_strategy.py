import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
