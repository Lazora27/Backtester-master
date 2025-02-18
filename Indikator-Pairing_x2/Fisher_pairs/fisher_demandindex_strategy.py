import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DemandIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DemandIndex': 1.0
        })
    )
