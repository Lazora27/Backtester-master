import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AverageTrueRange': 1.0
        })
    )
