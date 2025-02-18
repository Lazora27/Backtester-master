import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
