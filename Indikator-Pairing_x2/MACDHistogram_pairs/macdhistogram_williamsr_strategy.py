import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und WilliamsR
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'WilliamsR': 1.0
        })
    )
