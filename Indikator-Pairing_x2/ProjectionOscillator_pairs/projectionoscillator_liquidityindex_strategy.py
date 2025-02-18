import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
