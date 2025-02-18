import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
