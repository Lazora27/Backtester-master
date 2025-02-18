import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_RelativeVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und RelativeVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'RelativeVolatilityIndex': 1.0
        })
    )
