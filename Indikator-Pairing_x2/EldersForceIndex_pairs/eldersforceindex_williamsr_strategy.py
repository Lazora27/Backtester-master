import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
