import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
