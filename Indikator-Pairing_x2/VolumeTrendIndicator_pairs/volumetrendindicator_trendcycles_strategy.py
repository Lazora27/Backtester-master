import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
