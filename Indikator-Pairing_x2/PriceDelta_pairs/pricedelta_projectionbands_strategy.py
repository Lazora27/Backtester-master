import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ProjectionBands': 1.0
        })
    )
