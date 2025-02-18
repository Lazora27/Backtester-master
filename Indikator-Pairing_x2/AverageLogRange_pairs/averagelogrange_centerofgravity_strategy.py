import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'CenterOfGravity': 1.0
        })
    )
