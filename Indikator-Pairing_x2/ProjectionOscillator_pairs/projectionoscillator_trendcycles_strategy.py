import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
