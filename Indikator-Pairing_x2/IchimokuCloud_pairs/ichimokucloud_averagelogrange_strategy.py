import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'AverageLogRange': 1.0
        })
    )
