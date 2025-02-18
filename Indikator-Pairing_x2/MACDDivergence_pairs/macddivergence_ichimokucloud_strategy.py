import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'IchimokuCloud': 1.0
        })
    )
