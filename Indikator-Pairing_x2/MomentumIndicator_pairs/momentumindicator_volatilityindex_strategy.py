import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'VolatilityIndex': 1.0
        })
    )
