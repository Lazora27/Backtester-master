import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
