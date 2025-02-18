import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TrendCycles': 1.0
        })
    )
