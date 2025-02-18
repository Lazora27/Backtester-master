import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und MassIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'MassIndex': 1.0
        })
    )
