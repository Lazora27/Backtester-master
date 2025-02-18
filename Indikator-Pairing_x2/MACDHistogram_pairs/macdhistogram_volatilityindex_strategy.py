import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VolatilityIndex': 1.0
        })
    )
