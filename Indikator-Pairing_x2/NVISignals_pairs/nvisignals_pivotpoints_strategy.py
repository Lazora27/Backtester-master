import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PivotPoints
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PivotPoints': 1.0
        })
    )
