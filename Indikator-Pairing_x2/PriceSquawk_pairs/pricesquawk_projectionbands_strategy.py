import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ProjectionBands': 1.0
        })
    )
