import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'EaseOfMovement': 1.0
        })
    )
