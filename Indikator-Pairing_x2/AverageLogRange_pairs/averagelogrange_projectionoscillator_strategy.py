import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
