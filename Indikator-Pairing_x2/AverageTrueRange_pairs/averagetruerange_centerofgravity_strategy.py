import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'CenterOfGravity': 1.0
        })
    )
