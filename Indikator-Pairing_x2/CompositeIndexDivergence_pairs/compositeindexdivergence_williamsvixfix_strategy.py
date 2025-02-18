import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
