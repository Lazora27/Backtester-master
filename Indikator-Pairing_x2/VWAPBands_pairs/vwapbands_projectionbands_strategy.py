import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ProjectionBands': 1.0
        })
    )
