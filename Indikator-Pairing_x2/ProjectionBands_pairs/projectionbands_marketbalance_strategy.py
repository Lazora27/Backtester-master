import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'MarketBalance': 1.0
        })
    )
