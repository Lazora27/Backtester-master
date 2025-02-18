import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TrendCycles': 1.0
        })
    )
