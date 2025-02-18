import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'EaseOfMovement': 1.0
        })
    )
