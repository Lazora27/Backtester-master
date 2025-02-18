import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ProjectionBands': 1.0
        })
    )
