import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DemandIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DemandIndex': 1.0
        })
    )
