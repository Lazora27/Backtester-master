import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MomentumIndicator': 1.0
        })
    )
