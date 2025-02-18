import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
