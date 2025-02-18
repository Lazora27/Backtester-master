import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'IchimokuCloud': 1.0
        })
    )
