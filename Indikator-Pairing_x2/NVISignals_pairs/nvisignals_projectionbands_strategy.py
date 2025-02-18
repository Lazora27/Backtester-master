import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ProjectionBands': 1.0
        })
    )
