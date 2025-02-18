import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
