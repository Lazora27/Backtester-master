import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TimeCycle': 1.0
        })
    )
