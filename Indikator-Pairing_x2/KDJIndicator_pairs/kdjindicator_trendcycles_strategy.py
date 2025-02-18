import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
