import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'IchimokuCloud': 1.0
        })
    )
