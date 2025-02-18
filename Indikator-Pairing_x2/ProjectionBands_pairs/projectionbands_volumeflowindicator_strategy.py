import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
