import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ProjectionBands': 1.0
        })
    )
