import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VortexIndicator': 1.0
        })
    )
