import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'ProjectionBands': 1.0
        })
    )
