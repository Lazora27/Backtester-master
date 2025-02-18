import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
