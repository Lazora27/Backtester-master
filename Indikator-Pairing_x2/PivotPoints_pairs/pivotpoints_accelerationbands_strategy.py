import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AccelerationBands': 1.0
        })
    )
