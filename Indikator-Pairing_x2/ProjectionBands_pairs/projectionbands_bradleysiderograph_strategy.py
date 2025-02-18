import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'BradleySiderograph': 1.0
        })
    )
