import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'BradleySiderograph': 1.0
        })
    )
