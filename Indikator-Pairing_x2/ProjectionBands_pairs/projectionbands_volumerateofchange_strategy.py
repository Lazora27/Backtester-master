import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
