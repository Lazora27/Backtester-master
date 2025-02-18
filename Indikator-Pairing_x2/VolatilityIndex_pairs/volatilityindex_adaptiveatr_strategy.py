import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
