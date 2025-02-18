import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'TrueRange': 1.0
        })
    )
