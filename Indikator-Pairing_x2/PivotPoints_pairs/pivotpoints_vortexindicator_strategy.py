import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VortexIndicator': 1.0
        })
    )
