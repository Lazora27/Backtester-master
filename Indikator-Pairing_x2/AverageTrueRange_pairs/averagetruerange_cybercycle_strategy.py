import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'CyberCycle': 1.0
        })
    )
