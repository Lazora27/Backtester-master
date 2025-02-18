import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'AverageTrueRange': 1.0
        })
    )
