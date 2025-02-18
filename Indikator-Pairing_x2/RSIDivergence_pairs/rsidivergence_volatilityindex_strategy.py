import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolatilityIndex': 1.0
        })
    )
