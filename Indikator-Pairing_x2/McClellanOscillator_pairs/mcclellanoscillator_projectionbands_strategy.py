import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
