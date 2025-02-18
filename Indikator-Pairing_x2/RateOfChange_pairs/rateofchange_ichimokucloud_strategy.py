import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'IchimokuCloud': 1.0
        })
    )
