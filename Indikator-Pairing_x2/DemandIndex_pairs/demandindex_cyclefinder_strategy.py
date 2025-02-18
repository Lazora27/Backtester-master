import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
