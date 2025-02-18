import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AverageTrueRange': 1.0
        })
    )
