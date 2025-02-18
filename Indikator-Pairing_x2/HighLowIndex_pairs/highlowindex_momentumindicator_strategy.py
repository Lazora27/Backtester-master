import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MomentumIndicator': 1.0
        })
    )
