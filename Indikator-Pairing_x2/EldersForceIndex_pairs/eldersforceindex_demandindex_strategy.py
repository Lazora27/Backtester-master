import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
