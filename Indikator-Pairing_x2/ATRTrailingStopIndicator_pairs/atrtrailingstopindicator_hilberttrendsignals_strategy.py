import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ATRTrailingStopIndicator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ATRTrailingStopIndicator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ATRTrailingStopIndicator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
