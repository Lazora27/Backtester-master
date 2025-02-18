import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
