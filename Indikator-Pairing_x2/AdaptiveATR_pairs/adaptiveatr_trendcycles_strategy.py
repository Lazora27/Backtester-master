import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'TrendCycles': 1.0
        })
    )
