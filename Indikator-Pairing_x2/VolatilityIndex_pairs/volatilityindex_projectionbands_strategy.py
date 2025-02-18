import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
