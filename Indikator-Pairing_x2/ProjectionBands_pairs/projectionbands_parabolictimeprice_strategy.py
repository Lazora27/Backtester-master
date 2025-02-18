import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
