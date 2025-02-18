import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
