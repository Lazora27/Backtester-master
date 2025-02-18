import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'EaseOfMovement': 1.0
        })
    )
