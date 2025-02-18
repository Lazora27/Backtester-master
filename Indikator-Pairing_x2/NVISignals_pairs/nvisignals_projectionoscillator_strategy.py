import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
