import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
