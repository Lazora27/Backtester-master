import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'TrendCycles': 1.0
        })
    )
