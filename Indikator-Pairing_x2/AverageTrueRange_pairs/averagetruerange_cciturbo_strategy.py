import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'CCITurbo': 1.0
        })
    )
