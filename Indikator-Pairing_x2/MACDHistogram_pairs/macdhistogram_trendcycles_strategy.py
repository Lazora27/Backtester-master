import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TrendCycles': 1.0
        })
    )
