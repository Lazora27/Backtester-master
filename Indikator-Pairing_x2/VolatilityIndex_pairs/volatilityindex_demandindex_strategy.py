import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
