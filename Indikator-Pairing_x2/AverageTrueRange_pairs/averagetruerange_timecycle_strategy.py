import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TimeCycle': 1.0
        })
    )
