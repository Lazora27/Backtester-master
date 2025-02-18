import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
