import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
