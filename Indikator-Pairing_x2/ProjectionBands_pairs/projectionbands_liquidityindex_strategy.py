import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'LiquidityIndex': 1.0
        })
    )
