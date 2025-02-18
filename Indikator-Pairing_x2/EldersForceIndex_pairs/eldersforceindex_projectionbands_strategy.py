import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
