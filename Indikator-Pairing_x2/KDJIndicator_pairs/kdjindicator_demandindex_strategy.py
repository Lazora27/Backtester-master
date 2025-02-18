import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
