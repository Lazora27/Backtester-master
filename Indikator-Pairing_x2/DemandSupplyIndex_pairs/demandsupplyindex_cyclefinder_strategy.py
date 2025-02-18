import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
