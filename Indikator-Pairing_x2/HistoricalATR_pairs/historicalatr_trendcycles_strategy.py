import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TrendCycles': 1.0
        })
    )
