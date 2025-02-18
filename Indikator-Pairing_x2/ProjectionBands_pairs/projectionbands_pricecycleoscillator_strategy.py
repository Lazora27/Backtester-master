import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
