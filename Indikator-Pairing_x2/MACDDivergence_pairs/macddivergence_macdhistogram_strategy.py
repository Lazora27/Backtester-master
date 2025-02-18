import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MACDHistogram': 1.0
        })
    )
