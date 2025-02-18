import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
