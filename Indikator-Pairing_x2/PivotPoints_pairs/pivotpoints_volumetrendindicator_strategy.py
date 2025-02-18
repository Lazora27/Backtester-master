import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
