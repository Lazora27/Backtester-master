import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
